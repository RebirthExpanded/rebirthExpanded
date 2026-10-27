"""Espathra (SV07 69 -- JP SVI 026; English SCR/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="8acf04ef-bc19-59ee-9bdd-402ab7e7d2b9",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name",
    display_name="Espathra",
    searchable_by=["Espathra", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=955,
    abilities=[
        Attack(
            title="Psychic Flash",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
        ),
    ],
)
