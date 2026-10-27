"""Salazzle (SV07 24 -- JP SV7 014; English ASC/224, ASC/35, SCR/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _evolved_this_turn(ctx) -> bool:
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number


async def sudden_scorching(ctx):
    n = 3 if _evolved_this_turn(ctx) else 1
    hand = ctx.hand(ctx.opponent_id)
    k = min(n, len(hand))
    if k:
        await ctx.discard_from_hand(k, minimum=k, player_id=ctx.opponent_id, prompt=f"Discard {k} card(s) from your hand")


card = PokemonCardDef(
    guid="7361b8ac-f584-575e-b20b-7d09c41a1165",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name",
    display_name="Salazzle",
    searchable_by=["Salazzle", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=757,
    abilities=[
        Attack(
            title="Sudden Scorching",
            game_text="Your opponent discards a card from their hand. If this Pokémon evolved from Salandit during this turn, your opponent discards 2 more cards.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=sudden_scorching,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
