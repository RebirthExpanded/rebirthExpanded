"""Abomasnow (SV10 60 -- JP SV10 027; English DRI/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


def _two_grass(ctx) -> bool:
    return ac.count_energy("self", _PT.GRASS)(ctx) >= 2


card = PokemonCardDef(
    guid="05603b8a-02f9-51d6-9c1d-492e6fde6565",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Attack(
            title="Lunge Out",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
        Attack(
            title="Frozen Wood",
            game_text="If this Pokémon has 2 or more Grass Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=ac.bonus_if(_two_grass, 120),
        ),
    ],
)
