from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def psyspear(ctx):
    """120; with 2 extra Energy (5 or more attached), 120 to a Benched Pokemon too."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if bench and ctx.energy_units_on(ctx.attacker) >= 5:
        target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(120, target=target)

card = PokemonCardDef(
    guid="56afb26b-bea5-50c6-9340-cf98bfa0f30a",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=386,
    abilities=[
        Attack(
            title="Psyspear",
            game_text="If this Pok\u00e9mon has at least 2 extra Energy attached (in addition to this attack's cost), this attack also does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=psyspear,
        ),
    ],
)
