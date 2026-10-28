"""Staravia (SV1 149 -- JP SV1S 064; English SVI/149). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="af6549da-b4dd-5a49-9472-03369f7ca3e2",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    display_name="Staravia",
    searchable_by=["Staravia", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=149,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Wing Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Speed Dive",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
