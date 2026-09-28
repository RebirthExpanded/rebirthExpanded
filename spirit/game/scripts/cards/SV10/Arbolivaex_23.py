from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def oil_salvo(ctx):
    """Choose an opposing Pokemon 6 times; 20 per pick to each, no W/R."""
    picks = {}
    for i in range(6):
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            break
        target = await ctx.choose_pokemon(pool, f"Choose 1 of your opponent's Pokémon ({i + 1}/6)")
        if target is None:
            target = pool[0]
        picks[target.entity_id] = (target, picks.get(target.entity_id, (target, 0))[1] + 1)
    for target, times in picks.values():
        await ctx.deal_damage(20 * times, target=target,
                              ignore_weakness=True, ignore_resistance=True)


async def aroma_shot(ctx):
    """160. This Pokemon recovers from all Special Conditions."""
    await ctx.deal_damage()
    await ctx.cure_all_conditions(ctx.attacker)

card = PokemonCardDef(
    guid="b4a70b16-4ead-579e-8cd9-26c08e7d07ef",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbolivaex.Name",
    display_name="Arboliva ex",
    searchable_by=["Arboliva ex", "Stage 2", "ex", "Arbolivaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=23,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Oil Salvo",
            game_text="Choose 1 of your opponent's Pok\u00e9mon 6 times. (You can choose the same Pok\u00e9mon more than once.) For each time you chose a Pok\u00e9mon, do 20 damage to it. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.GRASS: 1},
            damage=0,
            effect=oil_salvo,
        ),
        Attack(
            title="Aroma Shot",
            game_text="This Pok\u00e9mon recovers from all Special Conditions.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=aroma_shot,
        ),
    ],
)
