"""Victreebel (SV035 71 -- JP SV2a 071; English MEW/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def slow_acting_acid(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d):
        return
    ts = ctx.session.turn_state
    ts.schedule_counters(d.entity_id, ts.turn_number + 1, 12, ctx.player_id, ctx.attacker.entity_id)


card = PokemonCardDef(
    guid="b2e25c7c-32f9-57bd-8686-951be5f2fc91",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=71,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Spit Up",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
        ),
        Attack(
            title="Slow-Acting Acid",
            game_text="At the end of your opponent's next turn, put 12 damage counters on the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=slow_acting_acid,
        ),
    ],
)
