"""Miraidon (SVP 148 -- JP SVI 023; English SVP/148). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4506952b-836d-5d6f-85c2-025372727fa7",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=148,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Attack(
            title="Electric Claws",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Mach Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
        ),
    ],
)
