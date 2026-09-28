from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


async def nullifying_zero(ctx):
    """A coin for each opposing Pokemon; 150 to each one that came up heads."""
    targets = list(ctx.opponent_pokemon_in_play())
    if not targets:
        return
    results = await ctx.flip_coins(len(targets), ctx.ability.title)
    for target, heads in zip(targets, results):
        if heads:
            await ctx.deal_damage(150, target=target)

card = PokemonCardDef(
    guid="88d5928b-59f0-5693-bf92-f6ada6b3e5b6",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaZygardeex.Name",
    display_name="Mega Zygarde ex",
    searchable_by=["Mega Zygarde ex", "Basic", "ex", "SV_Mega", "MegaZygardeex"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=47,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Gaia Wave",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Nullifying Zero",
            game_text="For each of your opponent's Pok\u00e9mon, flip a coin. If heads, this attack does 150 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 5},
            damage=0,
            effect=nullifying_zero,
        ),
    ],
)
