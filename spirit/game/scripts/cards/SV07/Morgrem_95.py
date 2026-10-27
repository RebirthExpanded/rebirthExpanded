"""Morgrem (SV07 95 -- JP SV7 065; English SCR/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="541ee210-f007-52eb-8e6c-36c27250cb01",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    display_name="Morgrem",
    searchable_by=["Morgrem", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Darkness Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
