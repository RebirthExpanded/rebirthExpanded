"""Shiinotic (SV08 9 -- JP SV7a 003; English SSP/194, SSP/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _calming_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    return board.active_pokemon(player_id) is pokemon and other is not None and board.active_pokemon(other) is not None


async def calming_light(ctx):
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="e5a5d85e-2849-576c-b9ea-27b1a581ca56",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name",
    display_name="Shiinotic",
    searchable_by=["Shiinotic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    family_id=755,
    abilities=[
        Ability(
            title="Calming Light",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may make your opponent's Active Pokémon Asleep.",
            activation=Activations.ONCE_PER_TURN,
            condition=_calming_condition,
            effect=calming_light,
        ),
        Attack(
            title="Spiral Rush",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.flip_damage(until_tails=True, bonus_per_heads=30),
        ),
    ],
)
