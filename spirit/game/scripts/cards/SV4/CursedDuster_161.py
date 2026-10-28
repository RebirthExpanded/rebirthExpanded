"""Cursed Duster (SV4 161 -- JP SV4M 061; English PAR/161). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.data_utils import Ability, Triggers
from spirit.game.card_effects.attacks_common import discard_random_from_hand


def _duster_applies(ctx) -> bool:
    attacker = getattr(ctx, "ko_attacker", None)
    return (bool(getattr(ctx, "ko_from_attack", False)) and attacker is not None
            and attacker.owning_player_id != ctx.source.owning_player_id)


async def _cursed_duster(ctx):
    await discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonToolCardDef(
    guid="c59c5f0e-2d49-53e6-b633-fb4196b9a4c3",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CursedDuster.Name",
    display_name="Cursed Duster",
    searchable_by=["Cursed Duster", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=161,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Cursed Duster",
            game_text="If the Pokémon this card is attached to is Knocked Out by damage from an attack from your opponent's Pokémon, discard a random card from your opponent's hand.",
            trigger=Triggers.ON_KNOCKED_OUT,
            trigger_applies=_duster_applies,
            effect=_cursed_duster,
        ),
    ],
)
