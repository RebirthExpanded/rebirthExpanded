from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import TurnDamageModifier
from spirit.game.card_effects.trainers import grant_recovery_ability


async def grant(ctx):
    """This turn, your Fighting Pokemon's attacks do 30 more damage to the
    opponent's Active Pokemon (before W/R). The discard-pile clause is the
    card's grant_recovery_ability, offered from the discard."""
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        30, ctx.player_id,
        source_predicate=lambda p: PokemonTypes.FIGHTING.value in (
            p.get_attribute(AttrID.POKEMON_TYPES) or []),
    ))


card = SupporterCardDef(
    guid="f53e3719-5220-5ebd-9254-216b6b23cab5",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grant.Name",
    display_name="Grant",
    searchable_by=["Grant", "Supporter"],
    subtypes=["Supporter"],
    collector_number=203,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=grant,
    abilities=[grant_recovery_ability()],
)
