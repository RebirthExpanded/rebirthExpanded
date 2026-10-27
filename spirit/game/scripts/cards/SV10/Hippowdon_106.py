"""Hippowdon (SV10 106 -- JP SVP 187; English DRI/106). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def super_sandstorm(ctx):
    await ctx.deal_damage()
    for pid in ctx.board.player_ids:
        for p in list(ctx.board.pokemon_in_play(pid)):
            if p._containing_area_name() == "bench" and _counters(ctx.board, p) > 0:
                await ctx.deal_damage(40, target=p)


card = PokemonCardDef(
    guid="a094df15-0d7e-561d-8da7-b6425842cf5a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=106,
    set_code="SV10",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
        ),
        Attack(
            title="Super Sandstorm",
            game_text="This attack also does 40 damage to each Benched Pokémon that has any damage counters on it (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=super_sandstorm,
        ),
    ],
)
