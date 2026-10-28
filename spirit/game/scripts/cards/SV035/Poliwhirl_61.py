"""Poliwhirl (SV035 61 -- JP SV2a 061; English MEW/176, MEW/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5a855782-56a2-5612-a486-259aae3d46e7",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    display_name="Poliwhirl",
    searchable_by=["Poliwhirl", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Wave Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Frog Hop",
            game_text="Flip a coin. If heads, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(60),
        ),
    ],
)
