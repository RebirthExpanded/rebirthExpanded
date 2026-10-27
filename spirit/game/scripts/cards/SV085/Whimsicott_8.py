"""Whimsicott (SV085 8 -- JP SV5K 008; English PRE/8, TEF/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def wafting_heal(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    a = ctx.board.active_pokemon(ctx.player_id)
    if a is None or not _of_type(a, PokemonTypes.GRASS) or not _counters(ctx.board, a):
        return
    if not await ctx.ask_yes_no("Use Wafting Heal?"):
        return
    await ctx.heal(10 * _counters(ctx.board, a), a)
    energy = list(ctx.attached_energies(a))
    if energy:
        await ctx.discard_cards(energy)


card = PokemonCardDef(
    guid="aa63ad76-2b2c-55a5-96df-913b51532658",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Ability(
            title="Wafting Heal",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may heal all damage from your Active Grass Pokémon. If you healed any damage in this way, discard all Energy from that Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=wafting_heal,
        ),
        Attack(
            title="Seed Bomb",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
    ],
)
