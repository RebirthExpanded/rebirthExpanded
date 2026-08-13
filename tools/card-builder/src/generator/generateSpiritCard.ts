import { getPrefabById } from '../prefabs/catalog';
import { MissingPrefabError, matchEffectText, matchedToSelected } from '../prefabs/matcher';
import { findServerEffect } from '../serverEffects';
import type {
  AttackDraft,
  CardDraft,
  EnergyShort,
  PrefabImport,
  PowerDraft,
  SelectedPrefab,
  ServerEffect,
} from '../types';
import { spiritSetCodeFromPtcgoOrId } from './setMapping';
import { cleanCardName, spiritGuidForCatalogId } from './uuid5';

const TYPE_ENUM: Record<EnergyShort, string> = {
  G: 'PokemonTypes.GRASS',
  R: 'PokemonTypes.FIRE',
  W: 'PokemonTypes.WATER',
  L: 'PokemonTypes.LIGHTNING',
  P: 'PokemonTypes.PSYCHIC',
  F: 'PokemonTypes.FIGHTING',
  D: 'PokemonTypes.DARKNESS',
  M: 'PokemonTypes.METAL',
  Y: 'PokemonTypes.FAIRY',
  N: 'PokemonTypes.DRAGON',
  C: 'PokemonTypes.COLORLESS',
  A: 'PokemonTypes.COLORLESS',
};

const STAGE_ENUM: Record<string, string> = {
  BASIC: 'PokemonStage.BASIC',
  STAGE_1: 'PokemonStage.STAGE1',
  STAGE_2: 'PokemonStage.STAGE2',
  VMAX: 'PokemonStage.VMAX',
  VSTAR: 'PokemonStage.VSTAR',
  VUNION: 'PokemonStage.VUNION',
  MEGA: 'PokemonStage.STAGE1',
  BREAK: 'PokemonStage.BREAK',
  LEGEND: 'PokemonStage.BASIC',
  LV_X: 'PokemonStage.STAGE1',
  RESTORED: 'PokemonStage.BASIC',
  NONE: 'PokemonStage.BASIC',
};

const RARITY_MAP: Record<string, string> = {
  Common: 'Rarities.Common',
  Uncommon: 'Rarities.Uncommon',
  Rare: 'Rarities.Rare',
  'Rare Holo': 'Rarities.RareHolo',
  'Rare Holo V': 'Rarities.RareHoloV',
  'Rare Holo VMAX': 'Rarities.RareHoloVMAX',
  'Rare Holo VSTAR': 'Rarities.RareHoloVSTAR',
  'Rare Holo EX': 'Rarities.RareHoloEX',
  'Double Rare': 'Rarities.RareHoloEX',
  'Rare Ultra': 'Rarities.RareUltra',
  'Rare Secret': 'Rarities.RareSecret',
  'Rare Rainbow': 'Rarities.RareRainbow',
  'Rare Promo': 'Rarities.RarePromo',
  Promo: 'Rarities.RarePromo',
  'Amazing Rare': 'Rarities.Amazing',
  'Radiant Rare': 'Rarities.RareRadiant',
  'Illustration Rare': 'Rarities.RareUltra',
  'Special Illustration Rare': 'Rarities.RareSecret',
  'Hyper Rare': 'Rarities.RareSecret',
  'ACE SPEC Rare': 'Rarities.Ace',
  'Ultra Rare': 'Rarities.RareUltra',
};

export function parseEnergyCost(input: string): EnergyShort[] {
  const cleaned = input.toUpperCase().replace(/ANY/g, 'A').replace(/[^GRWLPFDMYNCA]/g, '');
  return cleaned.split('') as EnergyShort[];
}

function pyStr(s: string): string {
  return JSON.stringify(s);
}

function mapRarity(raw: string): string {
  if (!raw) return 'Rarities.Common';
  if (RARITY_MAP[raw]) return RARITY_MAP[raw];
  if (/holo/i.test(raw)) return 'Rarities.RareHolo';
  if (/rare/i.test(raw)) return 'Rarities.Rare';
  if (/ace/i.test(raw)) return 'Rarities.Ace';
  return 'Rarities.Common';
}

function buildCostSrc(cost: string): string {
  const counts: Record<string, number> = {};
  for (const short of parseEnergyCost(cost)) {
    const enumRef = TYPE_ENUM[short] || 'PokemonTypes.COLORLESS';
    counts[enumRef] = (counts[enumRef] || 0) + 1;
  }
  return `{${Object.entries(counts).map(([k, v]) => `${k}: ${v}`).join(', ')}}`;
}

function mergeImports(imports: PrefabImport[]): string[] {
  const byModule = new Map<string, Set<string>>();
  for (const imp of imports) {
    if (!imp.module || !imp.names?.length) continue;
    const set = byModule.get(imp.module) ?? new Set();
    for (const n of imp.names) set.add(n);
    byModule.set(imp.module, set);
  }
  return [...byModule.entries()]
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([mod, names]) => `from ${mod} import ${[...names].sort().join(', ')}`);
}

function resolveSelectedEffect(
  selected: SelectedPrefab[],
  kind: 'attack' | 'power' | 'trainer',
  index: number,
  name: string
): { effectExpr?: string; activation?: string; imports: PrefabImport[]; needsUnimplemented: boolean } {
  const imports: PrefabImport[] = [];
  let effectExpr: string | undefined;
  let activation: string | undefined;
  let needsUnimplemented = false;

  for (const sel of selected) {
    const prefab = getPrefabById(sel.prefabId);
    if (!prefab) continue;
    const result = prefab.generateCall(sel.params, { kind, index, attackName: name, powerName: name });
    if (result.imports) imports.push(...result.imports);
    if (result.activation) activation = result.activation;
    if (result.effectExpr) {
      if (effectExpr && effectExpr !== result.effectExpr) {
        // Multiple effect bodies — fall back to unimplemented
        needsUnimplemented = true;
        effectExpr = undefined;
      } else {
        effectExpr = result.effectExpr;
      }
    }
  }
  return { effectExpr, activation, imports, needsUnimplemented };
}

function effectFromServer(server?: ServerEffect): { effectExpr?: string; imports: PrefabImport[]; helpers: string[] } {
  if (!server) return { imports: [], helpers: [] };
  const imports: PrefabImport[] = [];
  for (const line of server.imports) {
    const m = line.match(/^from\s+(\S+)\s+import\s+(.+)$/);
    if (m) {
      imports.push({
        module: m[1],
        names: m[2].split(',').map(s => s.trim()).filter(Boolean),
      });
    }
  }
  const body = server.body.filter(Boolean);
  // Prefer a single expression like "draw_attack(1)" or a name
  const joined = body.join('\n').trim();
  const exprMatch = joined.match(/^effect\s*=\s*(.+)$/m);
  const effectExpr = exprMatch ? exprMatch[1].trim() : body.length === 1 ? body[0].trim() : undefined;
  return { effectExpr, imports, helpers: server.helpers || [] };
}

function formatAttackBlock(
  attack: AttackDraft,
  index: number
): { lines: string[]; imports: PrefabImport[]; usesUnimplemented: boolean; helpers: string[] } {
  const imports: PrefabImport[] = [];
  const helpers: string[] = [];
  let usesUnimplemented = false;
  const lines: string[] = ['        Attack('];
  lines.push(`            title=${pyStr(attack.name)},`);
  if (attack.text.trim()) {
    lines.push(`            game_text=${pyStr(attack.text.trim())},`);
  }
  lines.push(`            cost=${buildCostSrc(attack.cost)},`);
  const damage = Number(attack.damage) || 0;
  if (damage) lines.push(`            damage=${damage},`);
  if (attack.damageCalculation === '+' || attack.damageCalculation === 'x') {
    lines.push(`            damage_operator=${pyStr(attack.damageCalculation)},`);
  }

  const text = attack.text.trim();
  if (text) {
    if (attack.serverEffect) {
      const fromServer = effectFromServer(attack.serverEffect);
      imports.push(...fromServer.imports);
      helpers.push(...fromServer.helpers);
      if (fromServer.effectExpr) {
        lines.push(`            effect=${fromServer.effectExpr},`);
      } else {
        lines.push('            effect=unimplemented,');
        usesUnimplemented = true;
      }
    } else {
      const resolved = resolveSelectedEffect(attack.selectedPrefabs, 'attack', index, attack.name);
      imports.push(...resolved.imports);
      if (resolved.needsUnimplemented || (!resolved.effectExpr && attack.selectedPrefabs.length === 0)) {
        lines.push('            effect=unimplemented,');
        usesUnimplemented = true;
      } else if (resolved.effectExpr) {
        lines.push(`            effect=${resolved.effectExpr},`);
      }
    }
  }
  lines.push('        ),');
  return { lines, imports, usesUnimplemented, helpers };
}

function formatAbilityBlock(
  power: PowerDraft,
  index: number
): { lines: string[]; imports: PrefabImport[]; usesUnimplemented: boolean; helpers: string[] } {
  const imports: PrefabImport[] = [];
  const helpers: string[] = [];
  let usesUnimplemented = false;
  const lines: string[] = ['        Ability('];
  lines.push(`            title=${pyStr(power.name)},`);
  if (power.text.trim()) {
    lines.push(`            game_text=${pyStr(power.text.trim())},`);
  }

  if (power.serverEffect) {
    const fromServer = effectFromServer(power.serverEffect);
    imports.push(...fromServer.imports);
    helpers.push(...fromServer.helpers);
    const resolved = resolveSelectedEffect(power.selectedPrefabs, 'power', index, power.name);
    imports.push(...resolved.imports);
    if (resolved.activation) {
      lines.push(`            activation=${resolved.activation},`);
      imports.push({ module: 'spirit.game.data_utils', names: ['Activations'] });
    } else if (/once during your turn/i.test(power.text) && power.useWhenInPlay) {
      lines.push('            activation=Activations.ONCE_PER_TURN,');
      imports.push({ module: 'spirit.game.data_utils', names: ['Activations'] });
    }
    if (fromServer.effectExpr) {
      lines.push(`            effect=${fromServer.effectExpr},`);
    } else {
      lines.push('            effect=unimplemented,');
      usesUnimplemented = true;
    }
  } else {
    const resolved = resolveSelectedEffect(power.selectedPrefabs, 'power', index, power.name);
    imports.push(...resolved.imports);
    if (resolved.activation) {
      lines.push(`            activation=${resolved.activation},`);
    } else if (/once during your turn/i.test(power.text) && power.useWhenInPlay) {
      lines.push('            activation=Activations.ONCE_PER_TURN,');
      imports.push({ module: 'spirit.game.data_utils', names: ['Activations'] });
    }
    if (resolved.needsUnimplemented || (!resolved.effectExpr && power.text.trim())) {
      lines.push('            effect=unimplemented,');
      usesUnimplemented = true;
    } else if (resolved.effectExpr) {
      lines.push(`            effect=${resolved.effectExpr},`);
    } else if (power.text.trim()) {
      lines.push('            effect=unimplemented,');
      usesUnimplemented = true;
    }
  }
  lines.push('        ),');
  return { lines, imports, usesUnimplemented, helpers };
}

function logicName(kind: 'pokemon' | 'trainer', safeName: string): string {
  return `com.direwolfdigital.cake.data.archetypes.${kind}.${safeName}.Name`;
}

function trainerClass(type: CardDraft['trainerType']): string {
  if (type === 'SUPPORTER') return 'SupporterCardDef';
  if (type === 'STADIUM') return 'StadiumCardDef';
  if (type === 'TOOL') return 'PokemonToolCardDef';
  return 'ItemCardDef';
}

export function scriptFileName(draft: CardDraft): string {
  const safe = cleanCardName(draft.name || draft.className || 'Card');
  const num = String(draft.setNumber || '0').replace(/^0+(?=\d)/, '') || '0';
  return `${safe}_${num}.py`;
}

export function resolveSpiritSetCode(draft: CardDraft): string {
  if (draft.spiritSetCode?.trim()) return draft.spiritSetCode.trim().toUpperCase();
  return spiritSetCodeFromPtcgoOrId(draft.set, draft.catalogId);
}

/**
 * Auto-fill selectedPrefabs from effect text when empty; fall back to similar scripts.
 */
export async function resolvePrefabs(draft: CardDraft): Promise<CardDraft> {
  const next: CardDraft = structuredClone(draft);

  if (next.hasAttacks) {
    for (const attack of next.attacks) {
      const text = attack.text.trim();
      if (!text) {
        attack.matchError = undefined;
        continue;
      }
      if (attack.selectedPrefabs.length > 0) {
        attack.matchError = undefined;
        attack.serverEffect = undefined;
        continue;
      }
      try {
        const matched = matchEffectText(text, 'attack');
        attack.selectedPrefabs = matchedToSelected(matched);
        attack.matchError = undefined;
        attack.serverEffect = undefined;
      } catch (e) {
        if (e instanceof MissingPrefabError) {
          attack.selectedPrefabs = [];
          attack.matchError = undefined;
          attack.serverEffect = await findServerEffect(text, 'attack');
          continue;
        }
        throw e;
      }
    }
  }

  if (next.hasPowers) {
    for (const power of next.powers) {
      const text = power.text.trim();
      if (!text) {
        power.matchError = undefined;
        continue;
      }
      if (power.selectedPrefabs.length > 0) {
        power.matchError = undefined;
        power.serverEffect = undefined;
        continue;
      }
      try {
        const matched = matchEffectText(text, 'power');
        power.selectedPrefabs = matchedToSelected(matched);
        power.matchError = undefined;
        power.serverEffect = undefined;
      } catch (e) {
        if (e instanceof MissingPrefabError) {
          power.selectedPrefabs = [];
          power.matchError = undefined;
          power.serverEffect = await findServerEffect(text, 'power');
          continue;
        }
        throw e;
      }
    }
  }

  if (next.extends === 'TrainerCard') {
    const text = next.trainerText.trim();
    if (text && next.trainerPrefabs.length === 0) {
      try {
        const matched = matchEffectText(text, 'trainer');
        next.trainerPrefabs = matchedToSelected(matched);
        next.trainerServerEffect = undefined;
      } catch (e) {
        if (e instanceof MissingPrefabError) {
          next.trainerPrefabs = [];
          next.trainerServerEffect = await findServerEffect(text, 'trainer');
        } else {
          throw e;
        }
      }
    }
  }

  if (next.extends === 'EnergyCard') {
    const text = next.energyText.trim();
    if (text && !next.energyServerEffect) {
      next.energyServerEffect = await findServerEffect(text, 'energy');
    }
  }

  return next;
}

export async function generateCardSource(draft: CardDraft): Promise<string> {
  const resolved = await resolvePrefabs(draft);
  const setCode = resolveSpiritSetCode(resolved);
  const safeName = cleanCardName(resolved.name || resolved.className || 'Card');
  const collector = Number(String(resolved.setNumber).replace(/\D/g, '')) || 0;
  const catalogId =
    resolved.catalogId ||
    `${setCode.toLowerCase()}-${resolved.setNumber}`;
  const guid = await spiritGuidForCatalogId(catalogId);
  const rarity = mapRarity(resolved.rarity);
  const subtypes = resolved.subtypes?.length
    ? resolved.subtypes
    : resolved.extends === 'PokemonCard'
      ? [resolved.stage === 'STAGE_1' ? 'Stage 1' : resolved.stage === 'STAGE_2' ? 'Stage 2' : 'Basic']
      : resolved.extends === 'TrainerCard'
        ? [resolved.trainerType === 'SUPPORTER' ? 'Supporter' : resolved.trainerType === 'STADIUM' ? 'Stadium' : resolved.trainerType === 'TOOL' ? 'Pokémon Tool' : 'Item']
        : [resolved.energyType === 'SPECIAL' ? 'Special' : 'Basic'];

  const searchable = [resolved.name, ...subtypes, safeName];
  const allImports: PrefabImport[] = [];
  const helperBlocks: string[] = [];
  let usesUnimplemented = false;

  if (resolved.extends === 'PokemonCard') {
    const abilityLines: string[] = [];
    if (resolved.hasPowers) {
      resolved.powers.forEach((p, i) => {
        const block = formatAbilityBlock(p, i);
        abilityLines.push(...block.lines);
        allImports.push(...block.imports);
        helperBlocks.push(...block.helpers);
        if (block.usesUnimplemented) usesUnimplemented = true;
      });
    }
    if (resolved.hasAttacks) {
      resolved.attacks.forEach((a, i) => {
        const block = formatAttackBlock(a, i);
        abilityLines.push(...block.lines);
        allImports.push(...block.imports);
        helperBlocks.push(...block.helpers);
        if (block.usesUnimplemented) usesUnimplemented = true;
      });
    }

    const dataNames = new Set<string>(['PokemonCardDef', 'Attack']);
    if (resolved.hasPowers) dataNames.add('Ability');
    if (usesUnimplemented) dataNames.add('unimplemented');
    for (const imp of allImports) {
      if (imp.module === 'spirit.game.data_utils') {
        for (const n of imp.names) dataNames.add(n);
      }
    }

    const attrNames = new Set<string>(['PokemonTypes', 'PokemonStage', 'Rarities']);
    for (const imp of allImports) {
      if (imp.module === 'spirit.game.attributes') {
        for (const n of imp.names) attrNames.add(n);
      }
    }

    const otherImports = mergeImports(
      allImports.filter(i => i.module !== 'spirit.game.data_utils' && i.module !== 'spirit.game.attributes')
    );

    const retreat = Math.max(0, parseEnergyCost(resolved.retreat).length);
    const element = TYPE_ENUM[resolved.cardType] || 'PokemonTypes.COLORLESS';
    const stage = STAGE_ENUM[resolved.stage] || 'PokemonStage.BASIC';

    const lines: string[] = [
      `from spirit.game.data_utils import ${[...dataNames].sort((a, b) => {
        const order = ['PokemonCardDef', 'Attack', 'Ability', 'Activations', 'unimplemented'];
        return (order.indexOf(a) === -1 ? 99 : order.indexOf(a)) - (order.indexOf(b) === -1 ? 99 : order.indexOf(b)) || a.localeCompare(b);
      }).join(', ')}`,
      `from spirit.game.attributes import ${[...attrNames].sort().join(', ')}`,
      ...otherImports,
      '',
    ];
    if (helperBlocks.length) {
      lines.push(...helperBlocks, '');
    }
    lines.push('card = PokemonCardDef(');
    lines.push(`    guid=${pyStr(guid)},`);
    lines.push(`    key=${pyStr(setCode)},`);
    lines.push(`    name=${pyStr(logicName('pokemon', safeName))},`);
    lines.push(`    display_name=${pyStr(resolved.name)},`);
    lines.push(`    searchable_by=${JSON.stringify(searchable)},`);
    lines.push(`    subtypes=${JSON.stringify(subtypes)},`);
    lines.push(`    collector_number=${collector},`);
    lines.push(`    set_code=${pyStr(setCode)},`);
    if (resolved.regulationMark) {
      lines.push(`    regulation_mark=${pyStr(resolved.regulationMark)},`);
    }
    lines.push(`    rarity=${rarity},`);
    lines.push(`    hp=${Number(resolved.hp) || 0},`);
    lines.push(`    elements=[${element}],`);
    lines.push(`    stage=${stage},`);
    lines.push(`    retreat_cost=${retreat},`);
    if (resolved.weaknessType) {
      lines.push(`    weakness_type=${TYPE_ENUM[resolved.weaknessType]},`);
    }
    if (resolved.resistanceType) {
      lines.push(`    resistance_type=${TYPE_ENUM[resolved.resistanceType]},`);
    }
    if (resolved.evolvesFrom) {
      lines.push(
        `    evolves_from=${pyStr(logicName('pokemon', cleanCardName(resolved.evolvesFrom)))},`
      );
    }
    if (resolved.familyId) {
      lines.push(`    family_id=${Number(resolved.familyId) || resolved.familyId},`);
    }
    if (abilityLines.length) {
      lines.push('    abilities=[');
      lines.push(...abilityLines);
      lines.push('    ],');
    }
    lines.push(')');
    return lines.join('\n') + '\n';
  }

  if (resolved.extends === 'TrainerCard') {
    const cls = trainerClass(resolved.trainerType);
    const dataNames = new Set<string>([cls]);
    let effectExpr: string | undefined;
    let helpers: string[] = [];

    if (resolved.trainerServerEffect) {
      const fromServer = effectFromServer(resolved.trainerServerEffect);
      allImports.push(...fromServer.imports);
      helpers = fromServer.helpers;
      effectExpr = fromServer.effectExpr;
    } else {
      const resolvedFx = resolveSelectedEffect(resolved.trainerPrefabs, 'trainer', 0, resolved.name);
      allImports.push(...resolvedFx.imports);
      effectExpr = resolvedFx.effectExpr;
      if (resolvedFx.needsUnimplemented) usesUnimplemented = true;
    }
    if (!effectExpr) {
      usesUnimplemented = true;
      effectExpr = 'unimplemented';
    }
    if (usesUnimplemented || effectExpr === 'unimplemented') dataNames.add('unimplemented');

    for (const imp of allImports) {
      if (imp.module === 'spirit.game.data_utils') {
        for (const n of imp.names) dataNames.add(n);
      }
    }
    const otherImports = mergeImports(
      allImports.filter(i => i.module !== 'spirit.game.data_utils' && i.module !== 'spirit.game.attributes')
    );

    const lines: string[] = [
      `from spirit.game.data_utils import ${[...dataNames].join(', ')}`,
      'from spirit.game.attributes import Rarities',
      ...otherImports,
      '',
    ];
    if (helpers.length) {
      lines.push(...helpers, '');
    }
    lines.push(`card = ${cls}(`);
    lines.push(`    guid=${pyStr(guid)},`);
    lines.push(`    key=${pyStr(setCode)},`);
    lines.push(`    name=${pyStr(logicName('trainer', safeName))},`);
    lines.push(`    display_name=${pyStr(resolved.name)},`);
    lines.push(`    searchable_by=${JSON.stringify(searchable)},`);
    lines.push(`    subtypes=${JSON.stringify(subtypes)},`);
    lines.push(`    collector_number=${collector},`);
    lines.push(`    set_code=${pyStr(setCode)},`);
    if (resolved.regulationMark) {
      lines.push(`    regulation_mark=${pyStr(resolved.regulationMark)},`);
    }
    lines.push(`    rarity=${rarity},`);
    if (resolved.trainerText.trim()) {
      // Prefer docstring on named effect when helpers present; else game text via comment
    }
    lines.push(`    effect=${effectExpr}`);
    lines.push(')');
    return lines.join('\n') + '\n';
  }

  // Energy
  {
    const isSpecial = resolved.energyType === 'SPECIAL';
    const energyType = TYPE_ENUM[(resolved.provides?.[0] as EnergyShort) || resolved.cardType] || 'PokemonTypes.COLORLESS';
    let effectImports: PrefabImport[] = [];
    let helpers: string[] = [];
    let grantedBlock = '';

    if (resolved.energyServerEffect) {
      const fromServer = effectFromServer(resolved.energyServerEffect);
      effectImports = fromServer.imports;
      helpers = fromServer.helpers;
      if (fromServer.effectExpr) {
        grantedBlock = fromServer.effectExpr;
      }
    }

    const lines: string[] = [
      'from spirit.game.data_utils import EnergyCardDef' + (grantedBlock || helpers.length ? ', Ability, Triggers' : ''),
      'from spirit.game.attributes import PokemonTypes, Rarities',
      ...mergeImports(effectImports),
      '',
    ];
    if (helpers.length) {
      lines.push(...helpers, '');
    }
    lines.push('card = EnergyCardDef(');
    lines.push(`    guid=${pyStr(guid)},`);
    lines.push(`    key=${pyStr(setCode)},`);
    lines.push(`    name=${pyStr(resolved.name)},`);
    lines.push(`    display_name=${pyStr(resolved.name)},`);
    lines.push(`    searchable_by=${JSON.stringify(searchable)},`);
    lines.push(`    subtypes=${JSON.stringify(subtypes)},`);
    lines.push(`    collector_number=${collector},`);
    lines.push(`    set_code=${pyStr(setCode)},`);
    if (resolved.regulationMark) {
      lines.push(`    regulation_mark=${pyStr(resolved.regulationMark)},`);
    }
    lines.push(`    rarity=${rarity},`);
    lines.push(`    energy_type=${energyType},`);
    lines.push(`    is_special=${isSpecial ? 'True' : 'False'}`);
    if (grantedBlock) {
      lines[lines.length - 1] += ',';
      lines.push(`    # Reused effect reference — review before committing`);
      lines.push(`    # effect_hint=${pyStr(grantedBlock)}`);
    }
    lines.push(')');
    return lines.join('\n') + '\n';
  }
}

/** Build a thin reprint stub when a sibling exists in the same set folder. */
export function generateReprintSource(
  draft: CardDraft,
  siblingFileName: string,
  rarityExpr?: string
): string {
  const collector = Number(String(draft.setNumber).replace(/\D/g, '')) || 0;
  const rarity = rarityExpr || mapRarity(draft.rarity);
  return [
    'from spirit.game.data_utils import reprint, sibling_card',
    'from spirit.game.attributes import Rarities',
    '',
    `card = reprint(sibling_card(__file__, ${pyStr(siblingFileName)}),`,
    `               collector_number=${collector}, rarity=${rarity})`,
    '',
  ].join('\n');
}
