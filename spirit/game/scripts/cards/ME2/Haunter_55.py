"""Haunter (ME2 55 -- JP MBG 002; English ASC/124, MEP/27, PFL/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="38cb0d43-a48f-57ee-8302-c450773acffa",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Spooky Shot",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
    ],
)
