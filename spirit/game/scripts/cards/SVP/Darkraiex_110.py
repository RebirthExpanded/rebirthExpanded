"""Darkrai ex (SVP 110 -- JP SVI 034; English SVP/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f51fdd2c-474c-51e6-b2a0-211f88e8752b",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkraiex.Name",
    display_name="Darkrai ex",
    searchable_by=["Darkrai ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=491,
    abilities=[
        Attack(
            title="Wind of Darkness",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Night Impact",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
