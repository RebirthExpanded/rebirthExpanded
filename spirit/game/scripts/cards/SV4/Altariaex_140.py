"""Altaria ex (SV4 140 -- JP SV4M 046; English PAR/140, PAR/232, PAR/253). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _humming_condition(board, player_id, pokemon) -> bool:
    return any(_counters(board, p) > 0 for p in board.pokemon_in_play(player_id))


async def humming_heal(ctx):
    for p in ctx.my_pokemon_in_play():
        await ctx.heal(20, p)


async def light_pulse(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, pc.attack_effect_shield_passive())


card = PokemonCardDef(
    guid="f3f15546-1544-5bca-8e11-293df9febc89",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altariaex.Name",
    display_name="Altaria ex",
    searchable_by=["Altaria ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=140,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Humming Heal",
            game_text="Once during your turn, you may heal 20 damage from each of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_humming_condition,
            effect=humming_heal,
        ),
        Attack(
            title="Light Pulse",
            game_text="During your opponent's next turn, prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=140,
            effect=light_pulse,
        ),
    ],
)
