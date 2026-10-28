"""Wugtrio (SV4 53 -- JP SV4K 025; English PAR/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_pokemon_tool


async def suddenly_select(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not ctx.deck_top(1) or not await ctx.ask_yes_no("Use Suddenly Select?"):
        return
    await su.search_to_hand(is_pokemon_tool, count=3, reveal=True, prompt="Choose up to 3 Pokémon Tool cards.")(ctx)


card = PokemonCardDef(
    guid="00b56025-7d6a-5052-b2e4-b48d924ba4ba",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name",
    display_name="Wugtrio",
    searchable_by=["Wugtrio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    family_id=960,
    abilities=[
        Ability(
            title="Suddenly Select",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may search your deck for up to 3 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=suddenly_select,
        ),
        Attack(
            title="Triple Whip",
            game_text="Flip 3 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=70),
        ),
    ],
)
