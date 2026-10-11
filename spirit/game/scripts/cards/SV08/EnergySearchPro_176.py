"""Energy Search Pro (SV - Surging Sparks 176/191 -- JP SV7a 052/064, the
art here).

Item -- ACE SPEC.

  "Search your deck for any number of Basic Energy cards of different
   types, reveal them, and put them into your hand. Then, shuffle your
   deck."

One deck-search browser with a pick slot per basic Energy type found in
the deck (Adventuring Lantern's shape), each "up to 1", so the picks are
always of different types.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import deck_nonempty, is_basic_energy_card
from spirit.game.data_utils import ItemCardDef

_BASIC_TYPES = [
    (PokemonTypes.GRASS, "Grass"), (PokemonTypes.FIRE, "Fire"),
    (PokemonTypes.WATER, "Water"), (PokemonTypes.LIGHTNING, "Lightning"),
    (PokemonTypes.PSYCHIC, "Psychic"), (PokemonTypes.FIGHTING, "Fighting"),
    (PokemonTypes.DARKNESS, "Darkness"), (PokemonTypes.METAL, "Metal"),
    (PokemonTypes.FAIRY, "Fairy"),
]


def _of_type(type_value):
    return lambda card: is_basic_energy_card(card) and energy_provides_type(card, type_value)


async def energy_search_pro(ctx):
    deck = ctx.deck()
    groups = [(_of_type(t.value), 1, f"Basic {name} Energy")
              for t, name in _BASIC_TYPES
              if any(_of_type(t.value)(c) for c in deck)]
    if groups:
        found = await ctx.search_deck_groups(
            groups, prompt="Choose Basic Energy cards of different types")
        picks = [c for group in found for c in group]
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    else:
        # Nothing to find, but the deck is still searched (and shuffled).
        await ctx.search_deck(is_basic_energy_card, count=1, minimum=0,
                              prompt="Choose Basic Energy cards of different types")
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="699f0a20-2f79-5f7e-8335-a89dd19bf649",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearchPro.Name",
    display_name="Energy Search Pro",
    searchable_by=["Energy Search Pro", "Item", "ACE SPEC", "EnergySearchPro"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=176,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    condition=deck_nonempty,
    effect=energy_search_pro,
)
