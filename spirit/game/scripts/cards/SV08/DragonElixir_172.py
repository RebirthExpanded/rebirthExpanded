"""Dragon Elixir (SV08 172 -- JP SV7a 057; English SSP/172). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10

from spirit.game.attributes import PokemonTypes


def _dragon_active_hurt(board, player_id, card=None) -> bool:
    a = board.active_pokemon(player_id)
    return a is not None and _of_type(a, PokemonTypes.DRAGON) and _counters(board, a) > 0


async def dragon_elixir(ctx):
    a = ctx.board.active_pokemon(ctx.player_id)
    if a is not None and _of_type(a, PokemonTypes.DRAGON):
        await ctx.heal(60, a)


card = ItemCardDef(
    guid="69b2a626-1c59-5901-be83-95849a9dd7d5",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragonElixir.Name",
    display_name="Dragon Elixir",
    searchable_by=["Dragon Elixir", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_dragon_active_hurt,
    effect=dragon_elixir,
)
