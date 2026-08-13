import { defineConfig, type Plugin } from 'vite';
import {
  createWriteStream,
  existsSync,
  mkdirSync,
  readFileSync,
  readdirSync,
  writeFileSync,
} from 'node:fs';
import { dirname, join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import type { IncomingMessage, ServerResponse } from 'node:http';
import { get as httpsGet } from 'node:https';
import { get as httpGet } from 'node:http';
import {
  SPIRIT_TO_TCG_SET_IDS,
} from './scripts/set-mapping.mjs';

// local helpers (avoid TS friction with .mjs named re-exports)
function spiritSetCodeFromCatalogId(catalogId: string): string {
  const dash = String(catalogId || '').indexOf('-');
  if (dash <= 0) return '';
  const setId = catalogId.slice(0, dash);
  for (const [spirit, ids] of Object.entries(SPIRIT_TO_TCG_SET_IDS as Record<string, string[]>)) {
    if (ids.includes(setId)) return spirit;
  }
  const sv = setId.match(/^sv(\d+)$/i);
  if (sv) return `SV${String(Number(sv[1])).padStart(2, '0')}`;
  const svpt = setId.match(/^sv(\d+)pt5$/i);
  if (svpt) return `SV${String(Number(svpt[1])).padStart(2, '0')}5`;
  return setId.toUpperCase();
}

const TCG_SET_ID_TO_SPIRIT: Record<string, string> = (() => {
  const map: Record<string, string> = {};
  for (const [spirit, ids] of Object.entries(SPIRIT_TO_TCG_SET_IDS as Record<string, string[]>)) {
    for (const id of ids) {
      if (!map[id]) map[id] = spirit;
    }
  }
  return map;
})();

const rootDir = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(rootDir, '../..');
const dataRoot = join(rootDir, 'data', 'pokemon-tcg-data');
const implementedCardIdsPath = join(rootDir, 'implementedCardIds.json');
const scriptsRoot = join(repoRoot, 'spirit/game/scripts/cards');
const assetsRoot = join(repoRoot, 'spirit/assets/cards');
const setsJsonPath = join(repoRoot, 'spirit/database/json_data/sets.json');

interface ScriptEffect {
  source: string;
  effectText: string;
  kind: 'attack' | 'power' | 'trainer' | 'energy';
  body: string[];
  imports: string[];
  similarity: number;
  helpers?: string[];
  fileName?: string;
  setCode?: string;
  displayName?: string;
  collectorNumber?: string;
}

function jsonResponse(res: ServerResponse, status: number, value: unknown): void {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.end(JSON.stringify(value));
}

function readRequestBody(req: IncomingMessage): Promise<string> {
  return new Promise((resolve, reject) => {
    const chunks: Buffer[] = [];
    req.on('data', chunk => chunks.push(Buffer.from(chunk)));
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

function collectPyFiles(dir: string): string[] {
  if (!existsSync(dir)) return [];
  return readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const path = join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === '__pycache__' || entry.name === 'CUSTOM') return [];
      return collectPyFiles(path);
    }
    return entry.name.endsWith('.py') && entry.name !== '__init__.py' ? [path] : [];
  });
}

function decodePyString(raw: string): string {
  try {
    return JSON.parse(raw.includes('"') || raw.startsWith("'") ? raw.replace(/^'/, '"').replace(/'$/, '"').replace(/\\'/g, "'") : raw);
  } catch {
    return raw.replace(/^['"]|['"]$/g, '').replace(/\\n/g, '\n').replace(/\\"/g, '"').replace(/\\'/g, "'");
  }
}

function extractImports(source: string): string[] {
  return source
    .split('\n')
    .map(l => l.trim())
    .filter(l => /^from\s+\S+\s+import\s+/.test(l) || /^import\s+/.test(l));
}

function extractHelpersBeforeCard(source: string): string[] {
  const cardIdx = source.search(/\ncard\s*=/);
  if (cardIdx < 0) return [];
  const preamble = source.slice(0, cardIdx);
  const lines = preamble.split('\n');
  const helpers: string[] = [];
  let capturing = false;
  let buf: string[] = [];
  for (const line of lines) {
    if (/^(async\s+)?def\s+/.test(line) || /^[A-Z_][A-Z0-9_]*\s*=/.test(line)) {
      if (buf.length) helpers.push(buf.join('\n'));
      buf = [line];
      capturing = true;
      continue;
    }
    if (capturing) {
      if (/^from\s|^import\s|^#/.test(line) && buf.length === 0) {
        capturing = false;
        continue;
      }
      if (line.trim() === '' && buf.length > 0 && !/^\s/.test(line)) {
        helpers.push(buf.join('\n'));
        buf = [];
        capturing = false;
      } else {
        buf.push(line);
      }
    }
  }
  if (buf.length) helpers.push(buf.join('\n'));
  return helpers.filter(h => /^(async\s+)?def\s+/.test(h.trim()));
}

function buildScriptEffects(): ScriptEffect[] {
  const effects: ScriptEffect[] = [];
  for (const file of collectPyFiles(scriptsRoot)) {
    const source = readFileSync(file, 'utf8');
    const rel = relative(scriptsRoot, file).replaceAll(sep, '/');
    const fileName = rel.split('/').pop() || '';
    const setCode =
      source.match(/set_code\s*=\s*["']([^"']+)["']/)?.[1] ||
      rel.split('/')[0] ||
      '';
    const displayName =
      source.match(/display_name\s*=\s*["']([^"']+)["']/)?.[1] ||
      source.match(/name\s*=\s*["']([^"']+)["']/)?.[1] ||
      '';
    const collectorNumber =
      source.match(/collector_number\s*=\s*(\d+)/)?.[1] ||
      fileName.match(/_(\d+)\.py$/)?.[1] ||
      '';
    const imports = extractImports(source);
    const helpers = extractHelpersBeforeCard(source);

    // Attack / Ability game_text + nearby effect=
    const abilityBlocks = [
      ...source.matchAll(
        /(?:Attack|Ability)\(\s*([\s\S]*?)(?=\n\s*(?:Attack|Ability)\(|\n\s*\],)/g
      ),
    ];
    for (const block of abilityBlocks) {
      const body = block[1] || '';
      const textRaw = body.match(/game_text\s*=\s*(("(?:\\.|[^"\\])*")|('(?:\\.|[^'\\])*'))/);
      if (!textRaw) continue;
      const effectText = decodePyString(textRaw[1]);
      if (!effectText.trim()) continue;
      const effectMatch = body.match(/effect\s*=\s*([^,\n]+)/);
      const effectExpr = effectMatch?.[1]?.trim();
      const isAttack = /Attack\s*\(\s*$/.test(source.slice(Math.max(0, (block.index || 0) - 20), block.index || 0) + 'Attack(') || body.includes('cost=') || body.includes('damage=');
      const kind: ScriptEffect['kind'] = body.includes('cost=') || /damage\s*=/.test(body) ? 'attack' : 'power';
      void isAttack;
      effects.push({
        source: rel,
        effectText,
        kind,
        body: effectExpr ? [effectExpr] : [],
        imports,
        similarity: 0,
        helpers: effectExpr && /^[a-z_][a-z0-9_]*$/i.test(effectExpr) ? helpers.filter(h => h.includes(`def ${effectExpr}`)) : [],
        fileName,
        setCode,
        displayName,
        collectorNumber,
      });
    }

    // Trainer / stadium top-level effect=
    if (/SupporterCardDef|ItemCardDef|StadiumCardDef|PokemonToolCardDef|FossilItemCardDef/.test(source)) {
      const effectMatch = source.match(/\n\s*effect\s*=\s*([A-Za-z_][\w.]*)/);
      const effectExpr = effectMatch?.[1]?.trim();
      let effectText = '';
      if (effectExpr && /^[a-z_][a-z0-9_]*$/i.test(effectExpr)) {
        const doc = source.match(
          new RegExp(
            `(?:async\\s+)?def\\s+${effectExpr}\\s*\\([^)]*\\)\\s*:\\s*\\n\\s*"""([\\s\\S]*?)"""`
          )
        );
        if (doc) effectText = doc[1].replace(/\s+/g, ' ').trim();
      }
      if (!effectText) {
        const rulesText = source.match(/"""([\s\S]*?)"""/)?.[1]?.trim();
        if (rulesText) effectText = rulesText.replace(/\s+/g, ' ').trim();
      }
      if (effectExpr && effectText) {
        effects.push({
          source: rel,
          effectText,
          kind: 'trainer',
          body: [effectExpr],
          imports,
          similarity: 0,
          helpers: helpers.filter(
            h =>
              h.includes(`def ${effectExpr}`) ||
              new RegExp(`def\\s+_${effectExpr}`).test(h)
          ),
          fileName,
          setCode,
          displayName,
          collectorNumber,
        });
      }
    }

    if (/EnergyCardDef/.test(source)) {
      const texts = [...source.matchAll(/game_text\s*=\s*(("(?:\\.|[^"\\])*")|('(?:\\.|[^'\\])*'))/g)];
      for (const t of texts) {
        const effectText = decodePyString(t[1]);
        const effectMatch = source.match(/effect\s*=\s*([^,\n]+)/);
        effects.push({
          source: rel,
          effectText,
          kind: 'energy',
          body: effectMatch ? [effectMatch[1].trim()] : [],
          imports,
          similarity: 0,
          helpers,
          fileName,
          setCode,
          displayName,
          collectorNumber,
        });
      }
    }
  }
  return effects;
}

function findReprintCandidates(spiritSet: string, name: string, excludeNumber = '') {
  const dir = join(scriptsRoot, spiritSet);
  if (!existsSync(dir)) return [];
  const normalizedName = name.trim().toLowerCase();
  const exclude = excludeNumber.trim();
  return collectPyFiles(dir)
    .map(filePath => {
      const source = readFileSync(filePath, 'utf8');
      const displayName =
        source.match(/display_name\s*=\s*["']([^"']+)["']/)?.[1] || '';
      const collectorNumber = source.match(/collector_number\s*=\s*(\d+)/)?.[1] || '';
      const fileName = filePath.split(/[/\\]/).pop() || '';
      return {
        className: fileName.replace(/\.py$/, ''),
        name: displayName,
        set: spiritSet,
        setNumber: collectorNumber,
        fullName: `${displayName} ${spiritSet}`,
        sourcePath: relative(scriptsRoot, filePath).replaceAll(sep, '/'),
        fileName,
      };
    })
    .filter(c => {
      if (c.name.trim().toLowerCase() !== normalizedName) return false;
      if (exclude && c.setNumber === exclude) return false;
      // Prefer full defs over reprint stubs as sources
      const src = readFileSync(join(scriptsRoot, c.sourcePath), 'utf8');
      return !/^\s*card\s*=\s*reprint\(/.test(src);
    });
}

function setExistsInCatalog(spiritCode: string): boolean {
  if (!existsSync(setsJsonPath)) return false;
  const sets = JSON.parse(readFileSync(setsJsonPath, 'utf8')) as Array<{ name: string }>;
  return sets.some(s => String(s.name).toUpperCase() === spiritCode.toUpperCase());
}

function downloadFile(url: string, dest: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const getter = url.startsWith('https') ? httpsGet : httpGet;
    const file = createWriteStream(dest);
    getter(url, res => {
      if (res.statusCode && res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        file.close();
        downloadFile(res.headers.location, dest).then(resolve, reject);
        return;
      }
      if (res.statusCode !== 200) {
        file.close();
        reject(new Error(`HTTP ${res.statusCode} for ${url}`));
        return;
      }
      res.pipe(file);
      file.on('finish', () => file.close(() => resolve()));
    }).on('error', err => {
      file.close();
      reject(err);
    });
  });
}

function resolveSpiritSet(payloadSet: string, catalogId?: string): string {
  const upper = (payloadSet || '').trim().toUpperCase();
  if (catalogId) {
    const fromCat = spiritSetCodeFromCatalogId(catalogId);
    if (fromCat) return fromCat;
  }
  if (SPIRIT_TO_TCG_SET_IDS[upper]) return upper;
  if (TCG_SET_ID_TO_SPIRIT[payloadSet?.toLowerCase()]) {
    return TCG_SET_ID_TO_SPIRIT[payloadSet.toLowerCase()];
  }
  return upper;
}

function spiritCardBuilderPlugin(): Plugin {
  return {
    name: 'spirit-card-builder-api',
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        const url = req.url?.split('?')[0] || '';

        if (url.startsWith('/tcg-data/')) {
          const rel = decodeURIComponent(url.slice('/tcg-data/'.length));
          const filePath = join(dataRoot, rel);
          if (!filePath.startsWith(dataRoot) || !existsSync(filePath)) {
            res.statusCode = 404;
            res.end('Not found');
            return;
          }
          if (filePath.endsWith('.json')) {
            res.setHeader('Content-Type', 'application/json; charset=utf-8');
          }
          res.end(readFileSync(filePath));
          return;
        }

        if (url === '/implemented-card-ids.json') {
          if (!existsSync(implementedCardIdsPath)) {
            jsonResponse(res, 200, { implementedCardIds: [] });
            return;
          }
          res.setHeader('Content-Type', 'application/json; charset=utf-8');
          res.end(readFileSync(implementedCardIdsPath));
          return;
        }

        if (url === '/server-card-effects.json') {
          try {
            jsonResponse(res, 200, buildScriptEffects());
          } catch (e) {
            jsonResponse(res, 500, { error: String(e) });
          }
          return;
        }

        if (url === '/reprint-candidates' && req.method === 'GET') {
          const u = new URL(req.url || '', 'http://localhost');
          const set = resolveSpiritSet(u.searchParams.get('set') || '');
          const name = u.searchParams.get('name')?.trim() || '';
          const excludeSetNumber = u.searchParams.get('excludeSetNumber')?.trim() || '';
          if (!set || !name) {
            jsonResponse(res, 400, { error: 'Set code and card name are required.' });
            return;
          }
          jsonResponse(res, 200, {
            candidates: findReprintCandidates(set, name, excludeSetNumber),
          });
          return;
        }

        if (url === '/save-card' && req.method === 'POST') {
          void (async () => {
            try {
              const payload = JSON.parse(await readRequestBody(req)) as {
                set?: string;
                catalogId?: string;
                fileName?: string;
                className?: string;
                source?: string;
                overwrite?: boolean;
                imageUrl?: string;
                downloadImage?: boolean;
                reprint?: {
                  fileName: string;
                  sourcePath: string;
                  name: string;
                  set: string;
                  setNumber: string;
                };
              };

              const spiritSet = resolveSpiritSet(payload.set || '', payload.catalogId);
              if (!/^[A-Z0-9][A-Z0-9_]*$/i.test(spiritSet)) {
                jsonResponse(res, 400, { error: 'Set code is invalid.' });
                return;
              }

              const dir = join(scriptsRoot, spiritSet);
              mkdirSync(dir, { recursive: true });
              mkdirSync(join(assetsRoot, spiritSet), { recursive: true });

              const inSetsJson = setExistsInCatalog(spiritSet);
              const warnings: string[] = [];
              if (!inSetsJson) {
                warnings.push(
                  `Set ${spiritSet} is not in spirit/database/json_data/sets.json — cards load from scripts but may be missing from the client catalog.`
                );
              }

              if (payload.reprint) {
                const sibling = payload.reprint.fileName;
                if (!sibling || !existsSync(join(dir, sibling))) {
                  jsonResponse(res, 400, { error: 'Reprint sibling script not found in set folder.' });
                  return;
                }
                const outName =
                  payload.fileName ||
                  `${String(payload.reprint.name || 'Card').replace(/[^a-zA-Z0-9]/g, '')}_${payload.reprint.setNumber}.py`;
                const outPath = join(dir, outName);
                if (existsSync(outPath) && !payload.overwrite) {
                  jsonResponse(res, 409, { error: 'File already exists.', path: outPath, warnings });
                  return;
                }
                if (!payload.source?.trim()) {
                  jsonResponse(res, 400, { error: 'Generated source is empty.' });
                  return;
                }
                writeFileSync(outPath, payload.source, 'utf8');
                let imagePath: string | undefined;
                if (payload.downloadImage !== false && payload.imageUrl) {
                  const stem = outName.replace(/\.py$/, '');
                  imagePath = join(assetsRoot, spiritSet, `${stem}.png`);
                  if (!existsSync(imagePath) || payload.overwrite) {
                    try {
                      await downloadFile(payload.imageUrl, imagePath);
                    } catch (e) {
                      warnings.push(`Image download failed: ${e}`);
                      imagePath = undefined;
                    }
                  }
                }
                jsonResponse(res, 200, {
                  message: `Saved reprint ${outName}`,
                  path: outPath,
                  imagePath,
                  warnings,
                  setRegistered: inSetsJson,
                });
                return;
              }

              const fileName =
                payload.fileName ||
                `${String(payload.className || 'Card').replace(/[^a-zA-Z0-9]/g, '')}_0.py`;
              if (!/^[A-Za-z0-9_]+\.py$/.test(fileName)) {
                jsonResponse(res, 400, { error: 'Invalid file name.' });
                return;
              }
              if (!payload.source?.trim()) {
                jsonResponse(res, 400, { error: 'Generated source is empty.' });
                return;
              }
              const outPath = join(dir, fileName);
              if (existsSync(outPath) && !payload.overwrite) {
                jsonResponse(res, 409, { error: 'File already exists.', path: outPath, warnings });
                return;
              }
              writeFileSync(outPath, payload.source, 'utf8');

              let imagePath: string | undefined;
              if (payload.downloadImage !== false && payload.imageUrl) {
                const stem = fileName.replace(/\.py$/, '');
                imagePath = join(assetsRoot, spiritSet, `${stem}.png`);
                if (!existsSync(imagePath) || payload.overwrite) {
                  try {
                    await downloadFile(payload.imageUrl, imagePath);
                  } catch (e) {
                    warnings.push(`Image download failed: ${e}`);
                    imagePath = undefined;
                  }
                }
              }

              jsonResponse(res, 200, {
                message: `Saved ${relative(repoRoot, outPath)}`,
                path: outPath,
                imagePath,
                warnings,
                setRegistered: inSetsJson,
              });
            } catch (e) {
              jsonResponse(res, 500, { error: String(e) });
            }
          })();
          return;
        }

        next();
      });
    },
  };
}

export default defineConfig({
  root: rootDir,
  server: {
    port: 5174,
    strictPort: true,
  },
  plugins: [spiritCardBuilderPlugin()],
});
