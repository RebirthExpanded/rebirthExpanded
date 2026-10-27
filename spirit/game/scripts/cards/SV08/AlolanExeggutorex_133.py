"""Alolan Exeggutor ex (SV08 133 -- JP SV7a 040; English SSP/133, SSP/225, SSP/242, SSP/248). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects.trainers import is_basic_energy_card

from spirit.game.session.effects import is_basic_pokemon_in_play


async def tropical_frenzy(ctx):
    await ctx.deal_damage()
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Attach any number of Basic Energy cards")
    for card in picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to attach it to")
        if target is not None:
            await ctx.attach_energy(card, target)


async def swinging_sphene(ctx):
    results = await ctx.flip_coins(1, "Swinging Sphene")
    if results and results[0]:
        d = ctx.opponent_active()
        if d is not None and is_basic_pokemon_in_play(d) and not ctx.effects_blocked(d):
            await ctx.knock_out(d)
    else:
        pool = [p for p in ctx.opponent_bench() if is_basic_pokemon_in_play(p) and not ctx.effects_blocked(p)]
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Benched Basic Pokémon to Knock Out") if pool else None
        if target is not None:
            await ctx.knock_out(target)


card = PokemonCardDef(
    guid="cc81a7e8-8d52-5082-8f4e-97f6c1eec04e",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorex.Name",
    display_name="Alolan Exeggutor ex",
    searchable_by=["Alolan Exeggutor ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=133,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Tropical Frenzy",
            game_text="You may attach any number of Basic Energy cards from your hand to your Pokémon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1},
            damage=150,
            effect=tropical_frenzy,
        ),
        Attack(
            title="Swinging Sphene",
            game_text="Flip a coin. If heads, Knock Out your opponent's Active Basic Pokémon. If tails, Knock Out 1 of your opponent's Benched Basic Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            effect=swinging_sphene,
        ),
    ],
)
