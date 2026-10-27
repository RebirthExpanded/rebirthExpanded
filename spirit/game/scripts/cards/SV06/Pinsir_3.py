"""Pinsir (SV06 3 -- JP SV5a 003; English TWM/168, TWM/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def slow_crunch(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool:
        await ctx.discard_cards(pool)
    d = ctx.opponent_active()
    if d is None or ctx.effects_blocked(d):
        return
    state = ctx.session.turn_state
    state.scheduled_knockouts[d.entity_id] = state.turn_number + 1


card = PokemonCardDef(
    guid="d185d16d-7060-5467-b0e7-da0817e63d8f",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Slow Crunch",
            game_text="Discard all Energy from this Pokémon. At the end of your opponent's next turn, the Defending Pokémon will be Knocked Out.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=slow_crunch,
        ),
        Attack(
            title="Superpowered Horns",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
