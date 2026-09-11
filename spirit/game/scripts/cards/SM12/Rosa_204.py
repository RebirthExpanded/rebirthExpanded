"""Rosa (SM - Cosmic Eclipse 204/236 -- JP SM11b 055/049).

Supporter.

  "You can play this card only if 1 of your Pokemon was Knocked Out during
   your opponent's last turn.
   Search your deck for a Pokemon, a Trainer card, and a basic Energy
   card, reveal them, and put them into your hand. Then, shuffle your
   deck."

The gate is ally_ko_last_turn, the clause Fezandipiti ex and Oricorio-GX
already read. The three cards come out of one browser with three labeled
slots, and any slot may come up empty.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import ally_ko_last_turn
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import (is_basic_energy, is_pokemon_card,
                                         is_trainer_card)


async def rosa(ctx):
    pokemon, trainers, energy = await ctx.search_deck_groups(
        [(is_pokemon_card, 1, "Pokémon"),
         (is_trainer_card, 1, "Trainer"),
         (is_basic_energy, 1, "basic Energy")],
        prompt="Choose a Pokémon, a Trainer card and a basic Energy card.")
    picks = list(pokemon) + list(trainers) + list(energy)
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="0f9744c7-54d2-5a96-9664-bbf1f6086bd2",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rosa.Name",
    display_name="Rosa",
    searchable_by=["Rosa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=rosa,
    condition=ally_ko_last_turn,
)
