"""Zacian V-UNION -- the combined Pokemon (SWSH Promos 163-166 -- JP
Special Card Set 009-012/013, the art here is the four pieces together).

Metal Pokemon V-UNION. HP 320, weakness Fire x2, resistance Grass -30,
retreat 2. When Knocked Out, the opponent takes 3 Prize cards.

  Union Gain                  [C]         Attach up to 2 [M] Energy cards
                                          from your discard pile to this
                                          Pokemon.
  Dance of the Crowned Sword  [MMC]  150  During your opponent's next turn,
                                          the Defending Pokemon's attacks do
                                          150 less damage (before applying
                                          Weakness and Resistance).
  Steel Cut                   [MMC]  200
  Master Blade                [MMMC] 340  Discard 3 Energy from this Pokemon.

Runtime-only: the four pieces (ZacianVUNION_163..166) name it and the
assembly rule on each builds it from the discard pile (session/legends.py).
Number 903 is this pool's own for the combined face.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.passives_common import debuff_defender_attacks
from spirit.game.card_effects.pokemon import union_gain_attack
from spirit.game.data_utils import Attack, VUnionPokemonDef

NAME = "com.direwolfdigital.cake.data.archetypes.pokemon.ZacianVUNION.Name"


UNION_GAIN = union_gain_attack(PokemonTypes.METAL)
DANCE_OF_THE_CROWNED_SWORD = Attack(
    title="Dance of the Crowned Sword",
    game_text="During your opponent's next turn, the Defending Pokémon's attacks do 150 less damage (before applying Weakness and Resistance).",
    cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
    damage=150,
    effect=debuff_defender_attacks(150),
)
STEEL_CUT = Attack(
    title="Steel Cut",
    game_text="",
    cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
    damage=200,
)
MASTER_BLADE = Attack(
    title="Master Blade",
    game_text="Discard 3 Energy from this Pokémon.",
    cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
    damage=340,
    effect=self_energy_discard_attack(3),
)


card = VUnionPokemonDef(
    guid="d0bd0de6-743d-5d20-a22c-f6b6ff64848b",
    key="Promo_SWSH",
    name=NAME,
    display_name="Zacian V-UNION",
    searchable_by=["Zacian V-UNION", "V-UNION", "ZacianVUNION"],
    subtypes=["V-UNION"],
    collector_number=903,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=320,
    elements=[PokemonTypes.METAL],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[UNION_GAIN, DANCE_OF_THE_CROWNED_SWORD, STEEL_CUT, MASTER_BLADE],
)
