from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import requires_damaged_pokemon


async def max_potion(ctx):
    """Heal all damage from 1 of your Pokémon. Then, discard all Energy from it."""
    candidates = [
        pokemon for pokemon in ctx.my_pokemon_in_play()
        if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
    if target is None:
        return
    await ctx.heal(ctx.max_hp(target), target)
    energies = list(ctx.attached_energies(target))
    if energies:
        await ctx.discard_cards(energies)


card = ItemCardDef(
    guid="b2dcfc2b-bf83-51aa-8674-1b9090ea73f2",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=max_potion,
    condition=requires_damaged_pokemon(),
)
