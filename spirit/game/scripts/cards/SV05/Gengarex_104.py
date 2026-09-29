from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers


async def gnawing_curse(ctx):
    """Arctozolt's Biting Whirlpool: 2 counters on the opponent's Pokemon
    they attach an Energy card to from hand."""
    if ctx.attaching_player_id == ctx.player_id:
        return
    receiver = ctx.energy_receiver
    if receiver is not None:
        await ctx.deal_damage(20, target=receiver, apply_modifiers=False, as_counters=True)


async def tricky_steps(ctx):
    """160; you may move an Energy from their Active to 1 of their Benched Pokemon."""
    await ctx.deal_damage()
    defender = ctx.defender
    bench = ctx.opponent_bench()
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies or not await ctx.ask_yes_no(
            "Move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon?"):
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.move_energy(picks[0], target)

card = PokemonCardDef(
    guid="a1a7c54f-4caa-51c6-9ab1-32e96f20e75d",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengarex.Name",
    display_name="Gengar ex",
    searchable_by=["Gengar ex", "Stage 2", "ex", "Gengarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=104,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Gnawing Curse",
            game_text="Whenever your opponent attaches an Energy card from their hand to 1 of their Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=gnawing_curse,
        ),
        Attack(
            title="Tricky Steps",
            game_text="You may move an Energy from your opponent's Active Pok\u00e9mon to 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=160,
            effect=tricky_steps,
        ),
    ],
)
