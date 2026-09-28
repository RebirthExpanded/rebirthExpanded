from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import guts_survive_passive


async def ghostly_blow(ctx):
    """100, then 5 damage counters on 1 of the opponent's Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(50, target=target, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="7e42ed3f-e928-50d6-bb18-5fc4b9b44dc1",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilape.Name",
    display_name="Annihilape",
    searchable_by=["Annihilape", "Stage 2", "Annihilape"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=56,
    abilities=[
        Ability(
            title="Durable Body",
            game_text="If this Pok\u00e9mon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pok\u00e9mon is not Knocked Out, and its remaining HP becomes 10.",
            passive=guts_survive_passive(hp_floor=10, title="Durable Body", flip=True),
        ),
        Attack(
            title="Ghostly Blow",
            game_text="Place 5 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=100,
            effect=ghostly_blow,
        ),
    ],
)
