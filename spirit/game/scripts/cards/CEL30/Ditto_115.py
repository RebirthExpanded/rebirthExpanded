from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card


async def surprisingly_transform(ctx):
    """Heads: swap in a Pokemon from the deck, keeping everything on this
    Pokemon (Palafin's identity_swap), Ditto goes into the deck; shuffle."""
    if not (await ctx.flip_coins(1, ctx.ability.title))[0]:
        return
    picks = await ctx.search_deck(is_pokemon_card, count=1, minimum=0,
                                  prompt="Choose a Pokémon to switch with this Pokémon.")
    if picks:
        await ctx.identity_swap(ctx.source, picks[0], destination="deck")
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="73046e94-7877-551d-b988-b9b764d3d82d",
    key="CEL30",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="CEL30",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Attack(
            title="Surprisingly Transform",
            game_text="Flip a coin. If heads, search your deck for a Pok\u00e9mon and switch it with this Pok\u00e9mon. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon. If you switched a Pok\u00e9mon in this way, put this card into your deck. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=0,
            effect=surprisingly_transform,
        ),
    ],
)
