from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_special_energy
from spirit.game.session.effects import is_special_energy


async def enhanced_hammer(ctx):
    """Discard a Special Energy attached to 1 of your opponent's Pok\u00e9mon."""
    candidates = [p for p in ctx.opponent_pokemon_in_play()
                  if any(is_special_energy(e) for e in ctx.attached_energies(p))]
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your opponent's Pok\u00e9mon")
    if target is not None:
        await ctx.discard_energy_from(target, 1, predicate=is_special_energy,
                                      prompt="Choose a Special Energy to discard")


card = ItemCardDef(
    guid="b0b7d30b-c42c-5e55-8717-5f93c027287c",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=176,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=enhanced_hammer,
    condition=opponent_has_special_energy
)
