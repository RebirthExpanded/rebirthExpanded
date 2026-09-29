from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import subtypes_for
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.session.effects import is_basic_energy


def _future(pokemon) -> bool:
    return "Future" in subtypes_for(pokemon.archetype_id)


async def peak_acceleration(ctx):
    """40, then up to 2 Basic Energy from the deck onto your Future Pokemon
    in any way you like; shuffle."""
    await ctx.deal_damage()
    targets = [p for p in ctx.my_pokemon_in_play() if _future(p)]
    if targets and ctx.deck():
        picks = await ctx.search_deck(is_basic_energy, count=2, minimum=0,
                                      prompt="Choose up to 2 Basic Energy cards.")
        if picks:
            await distribute_energy(ctx, picks, targets)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="7333c027-fee0-55bc-8272-72143f9c4d46",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic", "Future", "Miraidon"],
    subtypes=["Basic", "Future"],
    collector_number=121,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=1008,
    abilities=[
        Attack(
            title="Peak Acceleration",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to your Future Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=peak_acceleration,
        ),
        Attack(
            title="Sparking Strike",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.PSYCHIC: 1},
            damage=160,
        ),
    ],
)
