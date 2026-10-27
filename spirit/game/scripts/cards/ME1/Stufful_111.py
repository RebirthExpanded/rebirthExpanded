"""Stufful (ME1 111 -- JP M1S 055; English MEG/111, MEG/154). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="aabf4d05-c505-580c-847a-e83d605ecc63",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    display_name="Stufful",
    searchable_by=["Stufful", "Basic"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=759,
    abilities=[
        Attack(
            title="Light Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
