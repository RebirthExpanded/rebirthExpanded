"""Cobalion ex (ME4 64 -- JP M4 062; English CRI/103, CRI/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



def _metal_road_applies(ctx) -> bool:
    me = ctx.source
    return ctx.session.turn_state.active_player_id == ctx.player_id and any(
        is_energy_of_type(e, PokemonTypes.METAL)
        for p in ctx.my_pokemon_in_play() if p is not me for e in ctx.attached_energies(p))


async def metal_road(ctx):
    me = ctx.source
    pool = [e for p in ctx.my_pokemon_in_play() if p is not me
            for e in ctx.attached_energies(p) if is_energy_of_type(e, PokemonTypes.METAL)]
    if not pool or not await ctx.ask_yes_no("Use Metal Road?"):
        return
    picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Choose any amount of Metal Energy to move to this Pokémon")
    for energy in picks:
        await ctx.move_energy(energy, me)


card = PokemonCardDef(
    guid="87a5d8e7-23aa-54e0-8a8a-8ec276b3c1ff",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalionex.Name",
    display_name="Cobalion ex",
    searchable_by=["Cobalion ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=64,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=638,
    abilities=[
        Ability(
            title="Metal Road",
            game_text="Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may use this Ability. Move any amount of Metal Energy from your other Pokémon to this Pokémon.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            trigger_applies=_metal_road_applies,
            effect=metal_road,
        ),
        Attack(
            title="Power Tackle",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=_hit_then_lock,
        ),
    ],
)
