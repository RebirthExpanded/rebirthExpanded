"""Comfey (MF 16 -- JP MF 016; English 30C/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def comforting_aroma(ctx):
    damaged = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose a Benched Pokémon to heal 80 damage from")
    if target is not None:
        await ctx.heal(80, target)


card = PokemonCardDef(
    guid="c4387311-3224-5a68-870b-9aa0f7d4caea",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name",
    display_name="Comfey",
    searchable_by=["Comfey", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=764,
    abilities=[
        Attack(
            title="Comforting Aroma",
            game_text="Heal 80 damage from 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=comforting_aroma,
        ),
        Attack(
            title="Magical Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)
