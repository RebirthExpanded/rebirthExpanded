"""Bagon (SV09 112 -- JP SV9 070; English JTG/112). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="de6d32f1-f97c-5a16-a50c-9143f2a8ddb5",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon",
    searchable_by=["Bagon", "Basic"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=371,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=50,
            effect=ac.recoil_attack(10),
        ),
    ],
)
