"""Charizard (SM - Team Up 14/181 -- JP SM9 013/095).

Stage 2 Fire Pokemon, evolves from Charmeleon. HP 150, weakness Water x2,
retreat 2.

  Ability  Roaring Resolve  Once during your turn (before your attack), you
                            may put 2 damage counters on this Pokemon. If you
                            do, search your deck for up to 2 [R] Energy cards
                            and attach them to this Pokemon. Then, shuffle
                            your deck.
  Continuous Blaze Ball  [RR] 30+  Discard all [R] Energy from this Pokemon.
                            This attack does 50 more damage for each card you
                            discarded in this way.

"[R] Energy cards" searched out of the deck are basic Fire Energy cards;
"[R] Energy" discarded from this Pokemon is any attached Energy providing
Fire, counted as cards. The counters can Knock Out Charizard itself.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef

FIRE = PokemonTypes.FIRE.value


def _basic_fire_energy(card) -> bool:
    return is_basic_energy_card(card) and energy_provides_type(card, FIRE)


async def roaring_resolve(ctx):
    if not await ctx.ask_yes_no("Put 2 damage counters on this Pokémon?"):
        return
    await ctx.deal_damage(20, target=ctx.source, apply_modifiers=False, as_counters=True)
    picks = await ctx.search_deck(
        _basic_fire_energy, count=2, minimum=0,
        prompt="Choose up to 2 Fire Energy cards to attach to this Pokémon.",
    )
    for energy in picks:
        await ctx.attach_energy(energy, ctx.source)
    await ctx.shuffle_deck()


async def continuous_blaze_ball(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.source, 99, predicate=lambda e: energy_provides_type(e, FIRE),
        prompt="Discard all Fire Energy from this Pokémon",
    )
    await ctx.deal_damage(30 + 50 * len(discarded))


card = PokemonCardDef(
    guid="a0a74a24-9409-5f64-9e41-7b2d95fdb890",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Roaring Resolve",
            game_text="Once during your turn (before your attack), you may put 2 damage counters on this Pokémon. If you do, search your deck for up to 2 Fire Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=roaring_resolve,
        ),
        Attack(
            title="Continuous Blaze Ball",
            game_text="Discard all Fire Energy from this Pokémon. This attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            effect=continuous_blaze_ball,
        ),
    ],
)
