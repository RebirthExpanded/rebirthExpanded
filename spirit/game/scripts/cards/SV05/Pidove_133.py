from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.data_utils import def_for


def _unfezant(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) in ("Unfezant", "Unfezant ex")


def _emergency_condition(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return int(pokemon.get_attribute(AttrID.HP, 0) or 0) <= 30 and bool(deck and deck.children)


async def emergency_evolution(ctx):
    """HP 30 or less: evolve straight into Unfezant / Unfezant ex from the deck."""
    picks = await ctx.search_deck(_unfezant, count=1, minimum=0,
                                  prompt="Choose an Unfezant or Unfezant ex.")
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="0b967774-988b-5b6c-9d7e-d509b7e0a934",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove", "Basic", "Pidove"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=519,
    abilities=[
        Ability(
            title="Emergency Evolution",
            game_text="Once during your turn, if this Pok\u00e9mon's remaining HP is 30 or less, you may search your deck for an Unfezant or Unfezant ex and put it onto this Pidove to evolve it. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_emergency_condition,
            effect=emergency_evolution,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
