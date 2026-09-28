from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_basic_energy


def _basic_grass(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


async def buzzing_boost(ctx):
    """On moving Bench -> Active during your turn: up to 3 Basic [G] Energy
    from the deck onto this Pokemon, then shuffle."""
    if not ctx.deck() or not await ctx.ask_yes_no(
            "Search your deck for up to 3 Basic [G] Energy cards to attach to this Pokémon?"):
        return
    picks = await ctx.search_deck(_basic_grass, count=3, minimum=0,
                                  prompt="Choose up to 3 Basic [G] Energy cards.")
    for pick in picks:
        await ctx.attach_energy(pick, ctx.source)
    await ctx.shuffle_deck()


async def jet_cyclone(ctx):
    """210. Move 3 Energy from this Pokemon to 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = ctx.attached_energies(ctx.attacker)
    if not bench or not energies:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move 3 Energy to")
    if target is None:
        return
    count = min(3, len(energies))
    picks = await ctx.choose_cards(energies, count, minimum=count,
                                   prompt="Choose 3 Energy to move")
    for pick in picks:
        await ctx.move_energy(pick, target)

card = PokemonCardDef(
    guid="3e947917-c8ec-5568-9825-84b630f4a650",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmegaex.Name",
    display_name="Yanmega ex",
    searchable_by=["Yanmega ex", "Stage 1", "ex", "Yanmegaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=3,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Ability(
            title="Buzzing Boost",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may search your deck for up to 3 Basic [G] Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            effect=buzzing_boost,
        ),
        Attack(
            title="Jet Cyclone",
            game_text="Move 3 Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=jet_cyclone,
        ),
    ],
)
