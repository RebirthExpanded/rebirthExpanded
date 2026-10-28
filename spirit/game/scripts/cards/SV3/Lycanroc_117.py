"""Lycanroc (SV3 117 -- JP SV3 062; English OBF/117). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def finishing_fang(ctx):
    d = ctx.opponent_active()
    if d is not None and _counters(ctx.board, d) > 0:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="1df86a4f-43b8-5119-a138-dc63f7310404",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Attack(
            title="Finishing Fang",
            game_text="If your opponent's Active Pokémon has no damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=90,
            effect=finishing_fang,
        ),
        Attack(
            title="Slashing Claw",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
