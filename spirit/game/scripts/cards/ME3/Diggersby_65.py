from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def earthquake(ctx):
    """140, and 30 to each of your own Benched Pokemon."""
    await ctx.deal_damage()
    for pokemon in list(ctx.my_bench()):
        await ctx.deal_damage(30, target=pokemon)

card = PokemonCardDef(
    guid="dd515fc4-e95b-53d3-aeae-2e6dadbbd169",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diggersby.Name",
    display_name="Diggersby",
    searchable_by=["Diggersby", "Stage 1", "Diggersby"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    family_id=659,
    abilities=[
        Attack(
            title="Earthquake",
            game_text="This attack also does 30 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=earthquake,
        ),
        Attack(
            title="Whap Down",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
