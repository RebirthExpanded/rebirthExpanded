"""Roserade (BW - Dragons Exalted 15/124 -- JP Hydreigon Deck 30 002/015,
the art here).

Stage 1 Grass Pokemon (evolves from Roselia). HP 90, weakness Fire x2,
resistance Water -20, retreat 1.

  Le Parfum  (Ability)  When you play this Pokemon from your hand to evolve
                        1 of your Pokemon, you may search your deck for any
                        card and put it into your hand. Shuffle your deck
                        afterward.
  Squeeze    [GC] 30+   Flip a coin. If heads, this attack does 20 more
                        damage and the Defending Pokemon is now Paralyzed.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers


async def le_parfum(ctx):
    if not ctx.deck() or not await ctx.ask_yes_no(
            "Search your deck for any card and put it into your hand?"):
        return
    picks = await ctx.search_deck(None, count=1, minimum=0,
                                  prompt="Choose a card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="180108e0-6f4c-5691-a0b9-ceff32596acc",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    family_id=315,
    abilities=[
        Ability(
            title="Le Parfum",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may search your deck for any card and put it into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_EVOLVE,
            effect=le_parfum,
        ),
        Attack(
            title="Squeeze",
            game_text="Flip a coin. If heads, this attack does 20 more damage and the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True, heads_bonus_damage=20),
        ),
    ],
)
