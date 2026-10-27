"""Medicham (ME2PT5 104 -- JP M2a 085; English ASC/104, ASC/241). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _seven(ctx) -> bool:
    return len(ctx.hand()) == 7


card = PokemonCardDef(
    guid="5d43b950-90f0-5a59-a5aa-bd6338d86295",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Seventh Kick",
            game_text="If you don't have exactly 7 cards in your hand, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=150,
            effect=ac.bonus_if(_seven, 0, else_nothing=True),
        ),
    ],
)
