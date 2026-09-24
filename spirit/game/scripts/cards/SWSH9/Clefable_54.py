from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.card_effects.support_common import evolves_from, pokemon_can_still_evolve
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID



def _any_can_still_evolve(board, player_id, pokemon) -> bool:
    """Usable only with a Pokemon in play whose evolution can still come out
    of the deck (not every copy of it in the discard pile)."""
    return any(pokemon_can_still_evolve(board, player_id, p)
               for p in board.pokemon_in_play(player_id))


async def moonlit_miracle(ctx):
    flips = await ctx.flip_coins(3, "Moonlit Miracle")
    heads = sum(1 for r in flips if r)
    if heads == 0:
        return
    candidates = ctx.my_pokemon_in_play()
    if not candidates:
        return
    chosen = await ctx.choose_cards(
        candidates, heads, minimum=0,
        prompt=f"Choose up to {heads} of your Pokémon to evolve.",
    )
    if not chosen:
        return
    for pokemon in chosen:
        logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            continue
        picks = await ctx.search_deck(
            lambda c, name=logic_name: evolves_from(c, name),
            count=1, minimum=0,
            prompt="Choose a card that evolves from that Pokémon.",
        )
        if picks:
            await ctx.evolve_pokemon(pokemon, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="8991a2ec-eaeb-5c5f-aa46-4ced762274fd",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Attack(
            title="Moonlit Miracle",
            game_text="Flip 3 coins. Choose a number of your Pokémon in play up to the number of heads. For each of those Pokémon, search your deck for a card that evolves from that Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=_any_can_still_evolve,
            effect=moonlit_miracle,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
