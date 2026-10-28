"""Grapploct (SV045 52 -- JP SV4K 036; English PAF/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def slow_acting_syncope(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d):
        return
    ts = ctx.session.turn_state
    ts.scheduled_knockouts[d.entity_id] = ts.turn_number + 1


card = PokemonCardDef(
    guid="4c3ec5de-ca2e-5779-9f82-0c46fb33318a",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    abilities=[
        Attack(
            title="Slow-Acting Syncope",
            game_text="At the end of your opponent's next turn, the Defending Pokémon will be Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=slow_acting_syncope,
        ),
        Attack(
            title="Mach Cross",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
