"""Gogoat (SV1 12 -- JP SV1S 004; English SVI/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bb086fed-f0af-570b-80ad-28a7b1809356",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name",
    display_name="Gogoat",
    searchable_by=["Gogoat", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    family_id=672,
    abilities=[
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)
