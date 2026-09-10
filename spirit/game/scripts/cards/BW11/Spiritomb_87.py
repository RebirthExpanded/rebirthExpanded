"""Spiritomb (BW - Legendary Treasures 87/113 -- JP BW10 071/093).

Basic Darkness. HP 80, no weakness, no resistance, retreat 1.

  Ability  Sealing Scream  Each player can't play any ACE SPEC cards from
                           their hand.

  Hexed Mirror  [C]  Shuffle your hand into your deck. Then, draw a number
                     of cards equal to the number of cards in your
                     opponent's hand.

Sealing Scream is Vileplume's shape with a different filter and no side:
blocks_trainer_play refuses the play for BOTH players, this Spiritomb's
owner included, so a Computer Search or a Dowsing Machine sits in hand
while it is out. It is an Ability, so an ability lock switches it off.

Hexed Mirror is Judge from one side only, and the count is read after the
shuffle: with an empty opposing hand it draws nothing, which is the
printed outcome rather than a chain-rule refusal -- an attack can always be
declared.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.session.passives import Passive


class SealingScreamPassive(Passive):
    """Neither player may play an ACE SPEC card from hand."""

    def blocks_trainer_play(self, card, player_id, carrier):
        return "ACE SPEC" in subtypes_for(card.archetype_id)


async def hexed_mirror(ctx):
    """Your hand into the deck, then draw as many as they hold."""
    hand = ctx.hand()
    if hand:
        await ctx.shuffle_into_deck(hand)
    else:
        await ctx.shuffle_deck()
    await ctx.draw_cards(ctx.hand_size(ctx.opponent_id))


card = PokemonCardDef(
    guid="0f0db4da-bf1c-5500-adfd-fa5aeb0987a3",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Ability(
            title="Sealing Scream",
            game_text="Each player can't play any ACE SPEC cards from their hand.",
            passive=SealingScreamPassive(),
        ),
        Attack(
            title="Hexed Mirror",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=hexed_mirror,
        ),
    ],
)
