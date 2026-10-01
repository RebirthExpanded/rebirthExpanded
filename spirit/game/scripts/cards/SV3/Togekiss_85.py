from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers


def _precious_gift_applies(ctx) -> bool:
    """My turn is ending, fewer than 8 cards in hand, and a deck to draw."""
    return (ctx.session.turn_state.active_player_id == ctx.player_id
            and len(ctx.hand()) < 8 and bool(ctx.deck()))


async def precious_gift(ctx):
    """End of my turn: I may draw until I have 8 cards in hand. With
    Lillie's Full Force's end-of-turn shuffle also due, I pick the order."""
    if not _precious_gift_applies(ctx):
        return
    if not await ctx.ask_yes_no("Use Precious Gift and draw until you have 8 cards in your hand?"):
        return
    await ctx.draw_until(8)


async def power_cyclone(ctx):
    """110, then move an Energy from this Pokemon to 1 of your Benched
    Pokemon."""
    await ctx.deal_damage()
    energies = list(ctx.attached_energies(ctx.attacker))
    bench = list(ctx.my_bench())
    if not energies or not bench:
        return
    picks = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose an Energy to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move it to")
    if target is not None:
        await ctx.move_energy(picks[0], target)

card = PokemonCardDef(
    guid="bffbfb1d-615c-50a0-9da7-766cb209e511",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss", "Stage 2", "Togekiss"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Precious Gift",
            game_text="Once at the end of your turn (after your attack), you may use this Ability. Draw cards until you have 8 cards in your hand.",
            trigger=Triggers.END_OF_TURN,
            effect=precious_gift,
            trigger_applies=_precious_gift_applies,
        ),
        Attack(
            title="Power Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=power_cyclone,
        ),
    ],
)
