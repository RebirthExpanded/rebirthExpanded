"""Zigzagoon (SV3 167 -- JP SVG 022; English OBF/167). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="86746712-fbff-599d-8592-bb4f84453666",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    display_name="Zigzagoon",
    searchable_by=["Zigzagoon", "Basic"],
    subtypes=["Basic"],
    collector_number=167,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=263,
    abilities=[
        Attack(
            title="Headbutt Bounce",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
