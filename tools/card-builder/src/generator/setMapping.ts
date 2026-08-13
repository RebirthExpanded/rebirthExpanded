/** Spirit set folder ↔ pokemon-tcg-data set id (browser copy of scripts/set-mapping.mjs). */

export const SPIRIT_TO_TCG_SET_IDS: Record<string, string[]> = {
  SWSH1: ['swsh1'],
  SWSH2: ['swsh2'],
  SWSH3: ['swsh3'],
  SWSH35: ['swsh35'],
  SWSH4: ['swsh4'],
  SWSH45: ['swsh45', 'swsh45sv'],
  SWSH5: ['swsh5'],
  SWSH6: ['swsh6'],
  SWSH7: ['swsh7'],
  SWSH8: ['swsh8'],
  SWSH9: ['swsh9'],
  SWSH10: ['swsh10', 'swsh10tg'],
  SWSH11: ['swsh11', 'swsh11tg'],
  SWSH12: ['swsh12', 'swsh12tg'],
  CZ: ['swsh12pt5', 'swsh12pt5gg'],
  PGO: ['pgo'],
  CEL25: ['cel25', 'cel25c'],
  SV1: ['sv1'],
  SV01: ['sv1'],
  SV02: ['sv2'],
  SV03: ['sv3'],
  SV04: ['sv4'],
  SV05: ['sv5'],
  SV06: ['sv6'],
  SV065: ['sv6pt5'],
  SV07: ['sv7'],
  SV08: ['sv8'],
  SV085: ['sv8pt5'],
  SV09: ['sv9'],
  SV10: ['sv10'],
  BASE1: ['base1'],
  BW1: ['bw1'],
};

const TCG_TO_SPIRIT: Record<string, string> = (() => {
  const map: Record<string, string> = {};
  for (const [spirit, ids] of Object.entries(SPIRIT_TO_TCG_SET_IDS)) {
    for (const id of ids) {
      if (!map[id]) map[id] = spirit;
    }
  }
  return map;
})();

export function spiritSetCodeFromCatalogId(catalogId: string): string {
  const dash = String(catalogId || '').indexOf('-');
  if (dash <= 0) return '';
  const setId = catalogId.slice(0, dash);
  if (TCG_TO_SPIRIT[setId]) return TCG_TO_SPIRIT[setId];
  const sv = setId.match(/^sv(\d+)$/i);
  if (sv) return `SV${String(Number(sv[1])).padStart(2, '0')}`;
  const svpt = setId.match(/^sv(\d+)pt5$/i);
  if (svpt) return `SV${String(Number(svpt[1])).padStart(2, '0')}5`;
  return setId.toUpperCase();
}

export function spiritSetCodeFromPtcgoOrId(setField: string, catalogId?: string): string {
  if (catalogId) {
    const fromId = spiritSetCodeFromCatalogId(catalogId);
    if (fromId) return fromId;
  }
  const upper = String(setField || '').trim().toUpperCase();
  if (SPIRIT_TO_TCG_SET_IDS[upper]) return upper;
  // Already a Spirit code like SWSH12
  if (/^(SWSH|SV|BW|SM|XY|PGO|CZ|CEL)/i.test(upper)) return upper;
  // Reverse-lookup ptcgo → first spirit that maps (rare)
  return upper;
}
