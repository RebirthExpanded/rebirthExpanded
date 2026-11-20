"""Fight Arena (M7 78 -- JP M7 078/078 ファイトアリーナ). Japanese art.

Provisional English name and text (no English release yet).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, StadiumCardDef, Triggers
from spirit.game.card_effects import m7


card = StadiumCardDef(
    guid="e0c8e492-aed1-50b0-9bdb-981b90bbf492",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightArena.Name",
    display_name='Fight Arena',
    searchable_by=['Fight Arena', 'Stadium', 'FightArena'],
    subtypes=['Stadium'],
    collector_number=78,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Fight Arena",
        game_text="Once during each player's turn, that player may heal 20 damage from each of their Pokémon (excluding Pokémon with a Rule Box).",
        activation=Activations.ONCE_PER_TURN,
        condition=m7.fight_arena_condition,
        effect=m7.fight_arena,
    ),
)
