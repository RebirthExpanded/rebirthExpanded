"""Po Town (SM - Burning Shadows 121/147 -- JP SM3N 051/051, the art here).

Stadium.

  "Whenever any player plays a Pokemon from their hand to evolve 1 of their
   Pokemon, put 3 damage counters on that Pokemon."

An ON_POKEMON_EVOLVED watch: it goes off with the evolution's own "when
you play this Pokemon from your hand to evolve" Ability and the evolving
Pokemon's owner orders them -- Lycanroc-GX's Bloodthirsty Eyes first, or
the counters first, after which Mimikyu's Shadow Box leaves the damaged
Pokemon-GX without Abilities (official Q&A). A deck-sourced evolution
(Rare Candy from the deck, Wally) is not played from the hand.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, StadiumCardDef, Triggers


def _po_town_applies(ctx) -> bool:
    pokemon = getattr(ctx, "evolved_pokemon", None)
    if pokemon is None or not getattr(ctx, "evolved_from_hand", False):
        return False
    owner = pokemon.owning_player_id
    return owner is not None and pokemon in ctx.board.pokemon_in_play(owner)


async def po_town_watch(ctx):
    if _po_town_applies(ctx):
        await ctx.deal_damage(30, target=ctx.evolved_pokemon, apply_modifiers=False,
                              as_counters=True)


card = StadiumCardDef(
    guid="b7d8335a-6754-5658-90a7-11efd5febb01",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PoTown.Name",
    display_name="Po Town",
    searchable_by=["Po Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=121,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Po Town",
            game_text="Whenever any player plays a Pokémon from their hand to evolve 1 of their Pokémon, put 3 damage counters on that Pokémon.",
            trigger=Triggers.ON_POKEMON_EVOLVED,
            effect=po_town_watch,
            trigger_applies=_po_town_applies,
        ),
    ],
)
