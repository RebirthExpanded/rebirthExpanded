"""Farfetch'd (SV06 132 -- JP SV6 083; English TWM/132). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_pokemon_tool


async def impromptu_carrier(ctx):
    if not getattr(ctx, "benched_from_hand", True):
        return
    if any(is_pokemon_tool(c) for c in ctx.source.children):
        return
    if not ctx.deck_top(1) or not await ctx.ask_yes_no("Use Impromptu Carrier?"):
        return
    picks = await ctx.search_deck(is_pokemon_tool, count=1, minimum=0, prompt="Choose a Pokémon Tool card to attach to this Pokémon.")
    for card in picks:
        await ctx.attach_as_tool(card, ctx.source)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="a22cd6e1-884a-5994-8f72-5a177c1cca53",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=83,
    abilities=[
        Ability(
            title="Impromptu Carrier",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may search your deck for a Pokémon Tool card and attach it to this Pokémon. Then, shuffle your deck.",
            trigger=Triggers.ON_PLAY,
            effect=impromptu_carrier,
        ),
        Attack(
            title="Mach Cut",
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.discard_opponent_energy_attack(1, special_only=True),
        ),
    ],
)
