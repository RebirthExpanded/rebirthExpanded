"""Flareon (XY - Ancient Origins 13/98 -- JP XY7-B 006/069).

Stage 1 Fire Pokemon, evolves from Eevee. HP 90, weakness Water x2,
retreat 1.

  Ability  Flare Effect  As long as this Pokemon is in play, each of your
                         Stage 1 Pokemon is [R] type in addition to its
                         existing types.
  Heat Breath  [RCC] 60+  Flip a coin. If heads, this attack does 20 more
                          damage.

Vaporeon's Aqua Effect in Fire.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.pokemon import stage_one_type_grant
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

card = PokemonCardDef(
    guid="ccc0c675-9ebb-5eb6-829d-b8bcc3be44f8",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Flare Effect",
            game_text="As long as this Pokémon is in play, each of your Stage 1 Pokémon is [R] type in addition to its existing types.",
            passive=stage_one_type_grant(PokemonTypes.FIRE),
        ),
        Attack(
            title="Heat Breath",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_bonus(20),
        ),
    ],
)
