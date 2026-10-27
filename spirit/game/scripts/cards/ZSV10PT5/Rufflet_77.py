"""Rufflet (ZSV10PT5 77 -- JP SV11W 076; English BLK/154, BLK/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="a345b965-ce36-5948-ae79-884b0917685f",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    display_name="Rufflet",
    searchable_by=["Rufflet", "Basic"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=627,
    abilities=[
        Attack(
            title="Peck",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Glide",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
