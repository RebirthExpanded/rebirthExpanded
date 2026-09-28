from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_card, is_pokemon_of_type


async def spirit_burner(ctx):
    """Mill 5 of your own; 10 + 60 per Pokemon milled; then bench any of the
    milled [R] Basic Pokemon."""
    milled = ctx.deck_top(5)
    await ctx.discard_cards(milled)
    pokemon = [c for c in milled if is_pokemon_card(c)]
    await ctx.deal_damage(10 + 60 * len(pokemon))
    fire = [c for c in pokemon if is_basic_pokemon(c) and is_pokemon_of_type(c, PokemonTypes.FIRE)
            and c._containing_area_name() == "discard"]
    if fire:
        picks = await ctx.choose_cards(fire, len(fire), minimum=0,
                                       prompt="Put any number of the discarded [R] Pokémon onto your Bench")
        for pick in picks:
            await ctx.bench_pokemon(pick)

card = PokemonCardDef(
    guid="85b97637-b13b-525f-8122-bbed85efcc0d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=30,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Spirit Burner",
            game_text="Discard the top 5 cards of your deck. This attack does 60 more damage for each Pok\u00e9mon you discarded in this way. Then, put any number of [R] Pok\u00e9mon you discarded in this way onto your Bench.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=spirit_burner,
        ),
    ],
)
