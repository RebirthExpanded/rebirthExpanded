"""Ho-Oh (ME6A 7 -- JP M6a 007; English 30C/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def sacred_breath(ctx):
    pool = ctx.attached_energies(ctx.attacker)
    if pool:
        await ctx.discard_cards(list(pool))
    damaged = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    if damaged:
        target = await ctx.choose_pokemon(damaged, "Choose a Benched Pokémon to heal all damage from")
        if target is not None:
            await ctx.heal(10 * _counters(ctx.board, target), target)


card = PokemonCardDef(
    guid="5edb8a05-80d2-5da1-bc2b-1682196e2eb0",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Attack(
            title="Sacred Breath",
            game_text="Discard all Energy from this Pokémon. Heal all damage from 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            effect=sacred_breath,
        ),
        Attack(
            title="Fire Wing",
            game_text="",
            cost={PokemonTypes.FIRE: 3},
            damage=100,
        ),
    ],
)
