"""Raboot (SV07 27 -- JP SV7 017; English ASC/37, SCR/147, SCR/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="d7294798-c91e-5f5c-ad22-23fec6b6c763",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    display_name="Raboot",
    searchable_by=["Raboot", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    family_id=813,
    abilities=[
        Attack(
            title="Low Sweep",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
