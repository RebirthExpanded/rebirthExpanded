"""Rampardos ex (ME5 45 -- JP M5 043; English PBL/100, PBL/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def _flip_discard_energy(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target) \
            and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")



def _in_active(board, player_id, pokemon) -> bool:
    return board.active_pokemon(player_id) is pokemon


async def destructive_headbutting(ctx):
    results = await ctx.flip_coins(1, "Destructive Headbutting")
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target) \
            and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")


card = PokemonCardDef(
    guid="ed8b590b-dc93-50e2-8429-e647ced093db",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardosex.Name",
    display_name="Rampardos ex",
    searchable_by=["Rampardos ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=45,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=408,
    abilities=[
        Ability(
            title="Destructive Headbutting",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may use this Ability. Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_in_active,
            effect=destructive_headbutting,
        ),
        Attack(
            title="Rowdy Hammer",
            game_text="During your next turn, attacks used by this Pokémon do 150 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=150,
            effect=pc.boost_own_next_turn(150),
        ),
    ],
)
