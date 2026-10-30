"""Jirachi (SM - Team Up 99/181 -- JP SM8a 032/052).

Basic Metal Pokemon. HP 70, weakness Fire x2, resistance Psychic -20,
retreat 1.

  Ability  Stellar Wish  Once during your turn (before your attack), if this
                         Pokemon is your Active Pokemon, you may look at the
                         top 5 cards of your deck, reveal a Trainer card you
                         find there, and put it into your hand. Then, shuffle
                         the other cards back into your deck, and this
                         Pokemon is now Asleep.
  Slap  [MC] 30

Active-spot only, and the Sleep is the price: it lands whether or not a
Trainer turned up, which is why the ability is worth using only on a turn
this Pokemon is not attacking. The card is REVEALED on the way to the hand
("reveal a Trainer card you find there"), unlike the look-at-the-top-N
family that hands cards over face down.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_trainer_card

LOOK = 5


async def stellar_wish(ctx):
    """Top 5, a revealed Trainer into your hand, the rest shuffled back --
    and Asleep either way."""
    top = ctx.deck_top(LOOK)
    if top:
        trainers = [c for c in top if is_trainer_card(c)]
        picks = await ctx.choose_cards(
            trainers, 1, minimum=0,
            prompt="Choose a Trainer card to put into your hand.",
            display_cards=top if len(trainers) < len(top) else None,
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    await ctx.apply_special_condition(ctx.source, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="dc9a330b-7f83-53fa-b170-0a4a1edea705",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Ability(
            title="Stellar Wish",
            game_text="Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may look at the top 5 cards of your deck, reveal a Trainer card you find there, and put it into your hand. Then, shuffle the other cards back into your deck, and this Pokémon is now Asleep.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=stellar_wish,
        ),
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
