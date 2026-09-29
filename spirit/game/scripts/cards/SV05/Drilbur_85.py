from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_basic_energy


def _basic_fighting(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def dig_dig_dig(ctx):
    """Played from hand to the Bench: you may discard up to 3 Basic [F] Energy
    from your deck, then shuffle."""
    if not ctx.deck() or not await ctx.ask_yes_no(
            "Search your deck for up to 3 Basic [F] Energy cards to discard?"):
        return
    picks = await ctx.search_deck(_basic_fighting, count=3, minimum=0,
                                  prompt="Choose up to 3 Basic [F] Energy cards to discard.")
    if picks:
        await ctx.discard_cards(picks)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="f49b967c-40a8-51f0-8144-75a7307ab656",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur", "Basic", "Drilbur"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=529,
    abilities=[
        Ability(
            title="Dig Dig Dig",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for up to 3 Basic [F] Energy cards and discard them. Then, shuffle your deck.",
            trigger=Triggers.ON_PLAY,
            effect=dig_dig_dig,
        ),
        Attack(
            title="Sand Spray",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
