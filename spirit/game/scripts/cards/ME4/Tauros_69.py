from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for


async def target_together(ctx):
    """Choose an opposing Pokemon; a coin per Tauros in play; 50 per heads."""
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon") or ctx.defender
    count = sum(1 for p in ctx.my_pokemon_in_play()
                if "Tauros" in (getattr(def_for(p.archetype_id), "display_name", "") or ""))
    heads = sum(1 for r in await ctx.flip_coins(count, ctx.ability.title) if r) if count else 0
    if heads:
        await ctx.deal_damage(50 * heads, target=target)

card = PokemonCardDef(
    guid="ea2413e2-7bf5-57b4-b1f0-2c732a8995ef",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Tauros"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Target Together",
            game_text="Choose 1 of your opponent's Pok\u00e9mon and flip a coin for each of your Pok\u00e9mon in play that has \"Tauros\" in its name. This attack does 50 damage to the chosen Pok\u00e9mon for each heads. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=0,
            effect=target_together,
        ),
    ],
)
