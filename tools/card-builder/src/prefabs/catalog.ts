import type { PrefabDefinition, PrefabImport } from '../types';

const ATTACKS = 'spirit.game.card_effects.attacks_common';
const SUPPORT = 'spirit.game.card_effects.support_common';
const DATA = 'spirit.game.data_utils';
const ATTR = 'spirit.game.attributes';

function num(params: Record<string, string>, key: string, fallback = '0'): string {
  const raw = params[key];
  if (raw === undefined || raw === '') return fallback;
  return String(Number(raw));
}

function imp(module: string, ...names: string[]): PrefabImport[] {
  return [{ module, names }];
}

function effect(
  expr: string,
  imports: PrefabImport[],
  extras: Partial<PrefabDefinition['generateCall'] extends never ? never : ReturnType<PrefabDefinition['generateCall']>> = {}
) {
  return {
    lines: [expr],
    effectExpr: expr,
    imports,
    ...extras,
  };
}

/** Catalog of Spirit factory prefabs the builder may emit. */
export const PREFAB_CATALOG: PrefabDefinition[] = [
  // ── Ability activation marker ───────────────────────────────────────────
  {
    id: 'USE_ABILITY_ONCE_PER_TURN',
    name: 'ONCE_PER_TURN',
    description: 'Ability usable once per turn.',
    exampleTexts: ['Once during your turn…'],
    scope: 'power',
    importFrom: DATA,
    importNames: ['Activations'],
    params: [],
    patterns: [/^once during your turn\.?$/i],
    generateCall: () => ({
      lines: ['activation=Activations.ONCE_PER_TURN'],
      activation: 'Activations.ONCE_PER_TURN',
      imports: imp(DATA, 'Activations'),
    }),
  },

  // ── Drawing ─────────────────────────────────────────────────────────────
  {
    id: 'DRAW_CARDS',
    name: 'draw_attack / draw',
    description: 'Draw X cards.',
    exampleTexts: ['Draw a card.', 'Draw 2 cards.', 'Draw 3 cards.'],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['draw_attack'],
    params: [{ key: 'count', label: 'Cards', type: 'number', defaultValue: 1 }],
    patterns: [/^draw a card\.?$/i, /^draw (\d+) cards?\.?$/i],
    paramCaptures: { 1: 'count' },
    generateCall: (params) => {
      const count = params.count === undefined || params.count === '' ? '1' : num(params, 'count', '1');
      return effect(`draw_attack(${count})`, imp(SUPPORT, 'draw_attack'));
    },
  },
  {
    id: 'DRAW_UNTIL_HAND',
    name: 'draw_until_effect',
    description: 'Draw until you have X cards in hand.',
    exampleTexts: ['Draw cards until you have 6 cards in your hand.'],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['draw_until_effect'],
    params: [{ key: 'count', label: 'Hand size', type: 'number', defaultValue: 7 }],
    patterns: [
      /^draw(?: cards)? until you have (\d+) cards? in your hand\.?$/i,
      /^draw until you have (\d+) cards? in your hand\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params) => {
      const n = num(params, 'count', '7');
      return effect(`draw_until_effect(${n})`, imp(SUPPORT, 'draw_until_effect'));
    },
  },
  {
    id: 'DISCARD_THEN_DRAW',
    name: 'discard_then_draw',
    description: 'Discard X cards, then draw Y.',
    exampleTexts: ['Discard a card from your hand. If you do, draw 2 cards.'],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['discard_then_draw'],
    params: [
      { key: 'discard', label: 'Discard', type: 'number', defaultValue: 1 },
      { key: 'draw', label: 'Draw', type: 'number', defaultValue: 2 },
    ],
    patterns: [
      /^discard (?:a|1) card(?: from your hand)?\.?\s*(?:if you do,?\s*)?draw (\d+) cards?\.?$/i,
      /^discard (\d+) cards?(?: from your hand)?\.?\s*(?:if you do,?\s*)?draw (\d+) cards?\.?$/i,
    ],
    paramCaptures: { 1: 'draw' },
    generateCall: (params) => {
      const discard = params.discard && params.discard !== '' ? num(params, 'discard', '1') : '1';
      const draw = num(params, 'draw', '2');
      return effect(
        `discard_then_draw(${discard}, ${draw}, optional=False)`,
        imp(SUPPORT, 'discard_then_draw'),
      );
    },
  },

  // ── Special conditions ──────────────────────────────────────────────────
  {
    id: 'ACTIVE_NOW_PARALYZED',
    name: 'condition_attack(PARALYZED)',
    description: "Opponent's Active is now Paralyzed.",
    exampleTexts: ["Your opponent's Active Pokémon is now Paralyzed."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now paralyzed\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.PARALYZED)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'ACTIVE_NOW_ASLEEP',
    name: 'condition_attack(ASLEEP)',
    description: "Opponent's Active is now Asleep.",
    exampleTexts: ["Your opponent's Active Pokémon is now Asleep."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now asleep\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.ASLEEP)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'ACTIVE_NOW_CONFUSED',
    name: 'condition_attack(CONFUSED)',
    description: "Opponent's Active is now Confused.",
    exampleTexts: ["Your opponent's Active Pokémon is now Confused."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now confused\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.CONFUSED)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'ACTIVE_NOW_POISONED',
    name: 'condition_attack(POISONED)',
    description: "Opponent's Active is now Poisoned.",
    exampleTexts: ["Your opponent's Active Pokémon is now Poisoned."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now poisoned\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.POISONED)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'ACTIVE_NOW_BURNED',
    name: 'condition_attack(BURNED)',
    description: "Opponent's Active is now Burned.",
    exampleTexts: ["Your opponent's Active Pokémon is now Burned."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now burned\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.BURNED)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_PARALYZED',
    name: 'condition_attack(PARALYZED, flip)',
    description: 'Flip: if heads, Paralyzed.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Paralyzed.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now paralyzed\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.PARALYZED, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_ASLEEP',
    name: 'condition_attack(ASLEEP, flip)',
    description: 'Flip: if heads, Asleep.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Asleep.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now asleep\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.ASLEEP, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_POISONED',
    name: 'condition_attack(POISONED, flip)',
    description: 'Flip: if heads, Poisoned.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Poisoned.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now poisoned\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.POISONED, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_BURNED',
    name: 'condition_attack(BURNED, flip)',
    description: 'Flip: if heads, Burned.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Burned.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now burned\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.BURNED, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_CONFUSED',
    name: 'condition_attack(CONFUSED, flip)',
    description: 'Flip: if heads, Confused.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Confused.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now confused\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.CONFUSED, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },

  // ── Coin flip damage ────────────────────────────────────────────────────
  {
    id: 'FLIP_BONUS_DAMAGE',
    name: 'flip_bonus',
    description: 'Flip: if heads, do X more damage.',
    exampleTexts: ['Flip a coin. If heads, this attack does 30 more damage.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['flip_bonus'],
    params: [{ key: 'bonus', label: 'Bonus', type: 'number', defaultValue: 30 }],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*this attack does (\d+) more damage\.?$/i,
    ],
    paramCaptures: { 1: 'bonus' },
    generateCall: (params) =>
      effect(`flip_bonus(${num(params, 'bonus', '30')})`, imp(ATTACKS, 'flip_bonus')),
  },
  {
    id: 'FLIP_UNTIL_TAILS_PER_HEADS',
    name: 'flip_damage(until_tails)',
    description: 'Flip until tails; X damage per heads.',
    exampleTexts: ['Flip a coin until you get tails. This attack does 30 damage for each heads.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['flip_damage'],
    params: [{ key: 'per', label: 'Per heads', type: 'number', defaultValue: 30 }],
    patterns: [
      /^flip a coin until you get tails\.?\s*this attack does (\d+) damage for each heads\.?$/i,
    ],
    paramCaptures: { 1: 'per' },
    generateCall: (params) =>
      effect(
        `flip_damage(until_tails=True, per_heads=${num(params, 'per', '30')})`,
        imp(ATTACKS, 'flip_damage'),
      ),
  },
  {
    id: 'FLIP_UNTIL_TAILS_MORE_PER_HEADS',
    name: 'flip_damage(bonus until tails)',
    description: 'Flip until tails; +X more damage per heads.',
    exampleTexts: [
      'Flip a coin until you get tails. This attack does 30 more damage for each heads.',
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['flip_damage'],
    params: [{ key: 'per', label: 'Per heads', type: 'number', defaultValue: 30 }],
    patterns: [
      /^flip a coin until you get tails\.?\s*this attack does (\d+) more damage for each heads\.?$/i,
    ],
    paramCaptures: { 1: 'per' },
    generateCall: (params) =>
      effect(
        `flip_damage(until_tails=True, bonus_per_heads=${num(params, 'per', '30')})`,
        imp(ATTACKS, 'flip_damage'),
      ),
  },
  {
    id: 'FLIP_N_COINS_PER_HEADS',
    name: 'flip_damage(coins)',
    description: 'Flip N coins; X damage per heads.',
    exampleTexts: ['Flip 2 coins. This attack does 40 damage for each heads.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['flip_damage'],
    params: [
      { key: 'coins', label: 'Coins', type: 'number', defaultValue: 2 },
      { key: 'per', label: 'Per heads', type: 'number', defaultValue: 40 },
    ],
    patterns: [
      /^flip (\d+) coins?\.?\s*this attack does (\d+) damage for each heads\.?$/i,
    ],
    paramCaptures: { 1: 'coins', 2: 'per' },
    generateCall: (params) =>
      effect(
        `flip_damage(coins=${num(params, 'coins', '2')}, per_heads=${num(params, 'per', '40')})`,
        imp(ATTACKS, 'flip_damage'),
      ),
  },

  // ── Recoil / self damage ────────────────────────────────────────────────
  {
    id: 'RECOIL',
    name: 'recoil_attack',
    description: 'This Pokémon also does X damage to itself.',
    exampleTexts: ['This Pokémon also does 30 damage to itself.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['recoil_attack'],
    params: [{ key: 'amount', label: 'Self damage', type: 'number', defaultValue: 30 }],
    patterns: [
      /^this pok[eé]mon (?:also )?does (\d+) damage to itself\.?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(`recoil_attack(${num(params, 'amount', '30')})`, imp(ATTACKS, 'recoil_attack')),
  },

  // ── Snipe ───────────────────────────────────────────────────────────────
  {
    id: 'SNIPE_BENCH',
    name: 'snipe_attack(bench)',
    description: 'Deal X to 1 of opponent\'s Benched Pokémon.',
    exampleTexts: [
      "This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['snipe_attack'],
    params: [{ key: 'amount', label: 'Damage', type: 'number', defaultValue: 30 }],
    patterns: [
      /^this attack does (\d+) damage to 1 of your opponent'?s benched pok[eé]mon\.?(?:\s*\(don't apply weakness and resistance for benched pok[eé]mon\.\))?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(
        `snipe_attack(${num(params, 'amount', '30')}, pool="bench")`,
        imp(ATTACKS, 'snipe_attack'),
      ),
  },
  {
    id: 'SNIPE_ANY',
    name: 'snipe_attack(any)',
    description: 'Deal X to 1 of opponent\'s Pokémon.',
    exampleTexts: [
      "This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['snipe_attack'],
    params: [{ key: 'amount', label: 'Damage', type: 'number', defaultValue: 30 }],
    patterns: [
      /^this attack does (\d+) damage to 1 of your opponent'?s pok[eé]mon\.?(?:\s*\(don't apply weakness and resistance for benched pok[eé]mon\.\))?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(
        `snipe_attack(${num(params, 'amount', '30')}, pool="any")`,
        imp(ATTACKS, 'snipe_attack'),
      ),
  },

  // ── Heal ────────────────────────────────────────────────────────────────
  {
    id: 'HEAL_SELF',
    name: 'heal_attack',
    description: 'Heal X damage from this Pokémon.',
    exampleTexts: ['Heal 30 damage from this Pokémon.'],
    scope: 'attack',
    importFrom: SUPPORT,
    importNames: ['heal_attack'],
    params: [{ key: 'amount', label: 'Heal', type: 'number', defaultValue: 30 }],
    patterns: [/^heal (\d+) damage from this pok[eé]mon\.?$/i],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(`heal_attack(${num(params, 'amount', '30')})`, imp(SUPPORT, 'heal_attack')),
  },
  {
    id: 'HEAL_ITEM',
    name: 'heal_item',
    description: 'Heal X from 1 of your Pokémon.',
    exampleTexts: ['Heal 30 damage from 1 of your Pokémon.'],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['heal_item'],
    params: [{ key: 'amount', label: 'Heal', type: 'number', defaultValue: 30 }],
    patterns: [
      /^heal (\d+) damage from 1 of your pok[eé]mon\.?$/i,
      /^heal (\d+) damage from your active pok[eé]mon\.?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(`heal_item(${num(params, 'amount', '30')})`, imp(SUPPORT, 'heal_item')),
  },

  // ── Search ──────────────────────────────────────────────────────────────
  {
    id: 'SEARCH_BASIC_TO_BENCH',
    name: 'search_to_bench',
    description: 'Search for a Basic Pokémon and bench it.',
    exampleTexts: [
      'Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.',
    ],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['search_to_bench'],
    params: [{ key: 'count', label: 'Count', type: 'number', defaultValue: 1 }],
    patterns: [
      /^search your deck for (?:a|1) basic pok[eé]mon and put it onto your bench\.?\s*then,?\s*shuffle your deck\.?$/i,
      /^search your deck for up to (\d+) basic pok[eé]mon and put them onto your bench\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params) => {
      const count = params.count && params.count !== '' ? num(params, 'count', '1') : '1';
      return effect(`search_to_bench(count=${count})`, imp(SUPPORT, 'search_to_bench'));
    },
  },
  {
    id: 'SEARCH_TO_HAND',
    name: 'search_to_hand',
    description: 'Search deck for up to N cards into hand.',
    exampleTexts: [
      'Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.',
    ],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['search_to_hand'],
    params: [{ key: 'count', label: 'Count', type: 'number', defaultValue: 1 }],
    patterns: [
      /^search your deck for (?:a|1) card and put it into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
      /^search your deck for up to (\d+) cards? and put them into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params) => {
      const count = params.count && params.count !== '' ? num(params, 'count', '1') : '1';
      return effect(`search_to_hand(count=${count})`, imp(SUPPORT, 'search_to_hand'));
    },
  },

  // ── Switch / gust ───────────────────────────────────────────────────────
  {
    id: 'SWITCH_SELF',
    name: 'switch_self_attack',
    description: 'Switch this Pokémon with a Benched Pokémon.',
    exampleTexts: ['Switch this Pokémon with 1 of your Benched Pokémon.'],
    scope: 'attack',
    importFrom: SUPPORT,
    importNames: ['switch_self_attack'],
    params: [],
    patterns: [
      /^switch this pok[eé]mon with 1 of your benched pok[eé]mon\.?$/i,
    ],
    generateCall: () =>
      effect('switch_self_attack()', imp(SUPPORT, 'switch_self_attack')),
  },
  {
    id: 'GUST',
    name: 'gust_attack',
    description: "Switch in 1 of opponent's Benched Pokémon.",
    exampleTexts: [
      "Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
    ],
    scope: 'attack',
    importFrom: SUPPORT,
    importNames: ['gust_attack'],
    params: [],
    patterns: [
      /^switch (?:in )?1 of your opponent'?s benched pok[eé]mon(?: to the active spot)?\.?$/i,
      /^you may switch (?:in )?1 of your opponent'?s benched pok[eé]mon(?: to the active spot)?\.?$/i,
    ],
    generateCall: () => effect('gust_attack()', imp(SUPPORT, 'gust_attack')),
  },

  // ── Damage ignore effects ───────────────────────────────────────────────
  {
    id: 'DAMAGE_NOT_AFFECTED_BY_EFFECTS',
    name: 'plain (no effect hook)',
    description: "Damage isn't affected by effects on Active — often engine-native; leave stub.",
    exampleTexts: [
      "This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
    ],
    scope: 'attack',
    importFrom: '',
    importNames: [],
    params: [],
    patterns: [
      /^this attack'?s damage isn'?t affected by any effects on your opponent'?s active pok[eé]mon\.?$/i,
      /^this attack'?s damage isn'?t affected by weakness or resistance,? or by any effects on your opponent'?s active pok[eé]mon\.?$/i,
    ],
    generateCall: () => ({
      lines: ['# damage-ignore effects — implement manually if needed'],
      effectExpr: undefined,
      imports: [],
    }),
  },

  // ── Trainer draw helpers (Judge-like) ───────────────────────────────────
  {
    id: 'SHUFFLE_HAND_DRAW',
    name: 'shuffle_hand_into_deck_draw',
    description: 'Each player shuffles hand into deck and draws N.',
    exampleTexts: [
      'Each player shuffles their hand into their deck and draws 4 cards.',
    ],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['shuffle_hand_into_deck_draw'],
    params: [{ key: 'count', label: 'Draw', type: 'number', defaultValue: 4 }],
    patterns: [
      /^each player shuffles (?:their|his or her) hand into (?:their|his or her) deck and draws (\d+) cards?\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params) =>
      effect(
        `shuffle_hand_into_deck_draw(${num(params, 'count', '4')})`,
        imp(SUPPORT, 'shuffle_hand_into_deck_draw'),
      ),
  },
];

export function getPrefabById(id: string): PrefabDefinition | undefined {
  return PREFAB_CATALOG.find(p => p.id === id);
}

export function prefabsForScope(scope: string): PrefabDefinition[] {
  return PREFAB_CATALOG.filter(
    p => p.scope === 'both' || p.scope === scope
  );
}
