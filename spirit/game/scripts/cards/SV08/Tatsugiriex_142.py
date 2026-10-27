"""Tatsugiri ex (SV08 142 -- JP SV8 081; English SSP/142, SSP/226). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def cinnabar_lure(ctx):
    top = list(ctx.deck_top(10))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    pool = [c for c in top if is_basic_pokemon(c)]
    if pool and space > 0:
        picks = await ctx.choose_cards(pool, min(space, len(pool)), minimum=0, prompt="Choose any number of Pokémon to put onto your Bench")
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="cdbeb59c-5a6b-574a-b547-82535b72217c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiriex.Name",
    display_name="Tatsugiri ex",
    searchable_by=["Tatsugiri ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=142,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Surprise Pump",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=100,
            effect=ac.ignore_effects_attack(),
        ),
        Attack(
            title="Cinnabar Lure",
            game_text="Look at the top 10 cards of your deck. You may put any number of Pokémon you find there onto your Bench. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.DARKNESS: 1},
            effect=cinnabar_lure,
        ),
    ],
)
