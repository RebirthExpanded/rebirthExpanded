"""Nacli (SV2 121 -- JP SV2D 046; English PAF/176, PAL/121, PAL/220). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def salt_coating(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 20 damage from")
        if target is not None:
            await ctx.heal(20, target)


card = PokemonCardDef(
    guid="96830d9e-d305-5a2e-989d-a11a51d8d7a0",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    display_name="Nacli",
    searchable_by=["Nacli", "Basic"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=932,
    abilities=[
        Attack(
            title="Salt Coating",
            game_text="Heal 20 damage from 1 of your Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=salt_coating,
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
