"""Paldean Clodsire ex (SV045 59 -- JP SV1a 054; English PAF/219, PAF/59, PAL/130, PAL/244). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def _hit_flip_lock(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if results and not results[0]:
        ac.lock_all_attacks(ctx, ctx.attacker)


def _wetland_condition(board, player_id, pokemon) -> bool:
    area = board.find_global_area("activeStadium")
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    return bool(area and area.children) and other is not None and board.active_pokemon(other) is not None


async def toxic_wetland(ctx):
    d = ctx.opponent_active()
    if d is not None:
        await ctx.apply_special_condition(d, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="ab635359-af9e-5e72-8a85-168ffa7c920f",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsireex.Name",
    display_name="Paldean Clodsire ex",
    searchable_by=["Paldean Clodsire ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=59,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Ability(
            title="Toxic Wetland",
            game_text="Once during your turn, if a Stadium is in play, you may make your opponent's Active Pokémon Poisoned.",
            activation=Activations.ONCE_PER_TURN,
            condition=_wetland_condition,
            effect=toxic_wetland,
        ),
        Attack(
            title="Needle Bone",
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=_hit_flip_lock,
        ),
    ],
)
