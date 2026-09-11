from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.card_effects.support_common import pokemon_can_still_evolve
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities



def _can_still_evolve(board, player_id, pokemon) -> bool:
    """Usable only while an evolution of this Pokemon can still come out of
    the deck (not every copy of it in the discard pile)."""
    return pokemon_can_still_evolve(board, player_id, pokemon)


async def rocket_evolution(ctx):
    """Search a card that evolves from this Pokémon and put it onto this
    Pokémon to evolve it. Then, shuffle the deck."""
    await ctx.deal_damage()
    my_logic_name = ctx.source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def matches(c):
        return c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == my_logic_name

    picks = await ctx.search_deck(
        matches, count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="1b328806-47e1-5088-8d88-7d778d59b386",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    display_name="Pupitar",
    searchable_by=["Pupitar", "Stage 1", "Pupitar"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Sand Spray",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Rocket Evolution",
            game_text="Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            condition=_can_still_evolve,
            effect=rocket_evolution,
        ),
    ],
)
