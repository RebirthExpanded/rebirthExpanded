from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.pokemon import in_active_spot


async def scalding_steam(ctx):
    """Once during your turn, if this Pokemon is in the Active Spot, you may
    make your opponent's Active Pokemon Burned."""
    if await ctx.ask_yes_no("Make your opponent's Active Pokémon Burned?"):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


async def scorching_cyclone(ctx):
    """160. Move an Energy from this Pokemon to 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = ctx.attached_energies(ctx.attacker)
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy to move to 1 of your Benched Pokémon")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="513a070e-d578-5e79-93d7-53692a64a466",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanionex.Name",
    display_name="Volcanion ex",
    searchable_by=["Volcanion ex", "Basic", "ex", "Volcanionex"],
    subtypes=["Basic", "ex"],
    collector_number=31,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Ability(
            title="Scalding Steam",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may make your opponent's Active Pok\u00e9mon Burned.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=scalding_steam,
        ),
        Attack(
            title="Scorching Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=scorching_cyclone,
        ),
    ],
)
