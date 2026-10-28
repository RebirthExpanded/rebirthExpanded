"""Exploud (SV4 150 -- JP SV4K 057; English PAR/150). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _evolved_this_turn(ctx) -> bool:
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number

from spirit.game.session.effects import full_stack


async def sudden_shout(ctx):
    if not _evolved_this_turn(ctx):
        return
    d = ctx.opponent_active()
    if d is not None and not ctx.effects_blocked(d):
        await ctx.discard_cards(full_stack(d))


card = PokemonCardDef(
    guid="e69e2def-c9fa-5c16-861e-21d25b977f02",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name",
    display_name="Exploud",
    searchable_by=["Exploud", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=150,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Sudden Shout",
            game_text="Discard your opponent's Active Pokémon and all attached cards. If this Pokémon didn't evolve from Loudred during this turn, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=sudden_shout,
        ),
        Attack(
            title="Headbang",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)
