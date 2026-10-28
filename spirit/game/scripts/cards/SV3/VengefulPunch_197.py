"""Vengeful Punch (SV3 197 -- JP SV3 102; English OBF/197). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.data_utils import Ability, Triggers


def _punch_applies(ctx) -> bool:
    attacker = getattr(ctx, "ko_attacker", None)
    return (bool(getattr(ctx, "ko_from_attack", False)) and attacker is not None
            and attacker.owning_player_id != ctx.source.owning_player_id)


async def _vengeful_punch(ctx):
    attacker = getattr(ctx, "ko_attacker", None)
    if attacker is not None:
        await ctx.deal_damage(40, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)


card = PokemonToolCardDef(
    guid="48d5b10d-4d91-51b9-955a-ba67377d00d9",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VengefulPunch.Name",
    display_name="Vengeful Punch",
    searchable_by=["Vengeful Punch", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=197,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Vengeful Punch",
            game_text="If the Pokémon this card is attached to is Knocked Out by damage from an attack from your opponent's Pokémon, put 4 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_KNOCKED_OUT,
            trigger_applies=_punch_applies,
            effect=_vengeful_punch,
        ),
    ],
)
