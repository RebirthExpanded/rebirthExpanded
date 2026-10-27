"""Flabébé (SV06 86 -- JP SV5a 036; English TWM/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def bind_wound(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 30 damage from")
        if target is not None:
            await ctx.heal(30, target)


card = PokemonCardDef(
    guid="36c72e2e-4b99-50b3-afde-0f524fc3116c",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabebe.Name",
    display_name="Flabébé",
    searchable_by=["Flabébé", "Basic"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=669,
    abilities=[
        Attack(
            title="Bind Wound",
            game_text="Heal 30 damage from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bind_wound,
        ),
        Attack(
            title="Fairy Wind",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
