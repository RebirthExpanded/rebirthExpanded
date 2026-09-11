"""Vaporeon (XY - Ancient Origins 22/98 -- JP XY7-B 010/069).

Stage 1 Water Pokemon, evolves from Eevee. HP 90, weakness Grass x2,
retreat 2.

  Ability  Aqua Effect  As long as this Pokemon is in play, each of your
                        Stage 1 Pokemon is [W] type in addition to its
                        existing types.
  Hydro Splash  [WCC] 70

The type is added to the live type list (modify_pokemon_types), which is
what the damage step reads for Weakness and Resistance: a Stage 1 with [W]
added hits a Water-weak Pokemon for double, and runs into Water
Resistance, whichever of its types the printed one is. Vaporeon is a
Stage 1 too, so it counts itself (already Water).
"""

from spirit.game.attributes import (AttrID, PokemonStage, PokemonTypes,
                                    Rarities)
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class AquaEffectPassive(Passive):
    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return types
        if pokemon.get_attribute(AttrID.STAGE) != PokemonStage.STAGE1.value:
            return types
        if PokemonTypes.WATER.value in types:
            return types
        return list(types) + [PokemonTypes.WATER.value]


card = PokemonCardDef(
    guid="ac735f29-b4bb-5a4f-8d65-a0ed8ee5b902",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Aqua Effect",
            game_text="As long as this Pokémon is in play, each of your Stage 1 Pokémon is [W] type in addition to its existing types.",
            passive=AquaEffectPassive(),
        ),
        Attack(title="Hydro Splash", game_text="",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=70),
    ],
)
