from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def permeating_chill(ctx):
    """30, then 9 damage counters on the Defending Pokemon at the end of the
    opponent's next turn (gone if it leaves the Active Spot or evolves)."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.schedule_counters(defender, 9)

card = PokemonCardDef(
    guid="76b6b3a0-6b45-5f71-90b3-4adb5447e23f",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    display_name="Glaceon",
    searchable_by=["Glaceon", "Stage 1", "Glaceon"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Permeating Chill",
            game_text="At the end of your opponent's next turn, put 9 damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=permeating_chill,
        ),
        Attack(
            title="Icicle Missile",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
