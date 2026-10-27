"""Applin (SV08 138 -- JP SV7a 045; English SSP/138). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def nutrients(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 30 damage from")
        if target is not None:
            await ctx.heal(30, target)


card = PokemonCardDef(
    guid="aef9f16b-959a-5ce0-b77f-9f24d1ae6961",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    display_name="Applin",
    searchable_by=["Applin", "Basic"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=840,
    abilities=[
        Attack(
            title="Nutrients",
            game_text="Heal 30 damage from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=nutrients,
        ),
        Attack(
            title="Trip Over",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
    ],
)
