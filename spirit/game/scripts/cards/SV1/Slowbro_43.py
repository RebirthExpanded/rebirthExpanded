"""Slowbro (SV1 43 -- JP SV1V 020; English PAF/117, SVI/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10



def _strange_condition(board, player_id, pokemon) -> bool:
    return any(p is not pokemon and _counters(board, p) > 0 for p in board.pokemon_in_play(player_id))


async def strange_behavior(ctx):
    me = ctx.source
    pool = [p for p in ctx.my_pokemon_in_play() if p is not me and _counters(ctx.board, p) > 0]
    if not pool:
        return
    source = await ctx.choose_pokemon(pool, "Choose a Pokémon to move a damage counter from")
    if source is not None:
        await ctx.move_damage_counters(source, me, max_count=1)


card = PokemonCardDef(
    guid="317e2afd-ad18-531e-ba7e-c84407e186c2",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Strange Behavior",
            game_text="As often as you like during your turn, you may move 1 damage counter from 1 of your other Pokémon to this Pokémon.",
            activation=Activations.UNLIMITED,
            condition=_strange_condition,
            effect=strange_behavior,
        ),
        Attack(
            title="Bubble Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=su.heal_attack(30),
        ),
    ],
)
