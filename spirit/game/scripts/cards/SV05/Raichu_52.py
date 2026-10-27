"""Raichu (SV05 52 -- JP SV5M 024; English TEF/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def collateral_bolts(ctx):
    for pid in ctx.board.player_ids:
        for p in list(ctx.board.pokemon_in_play(pid)):
            if p is not ctx.attacker and _counters(ctx.board, p) > 0:
                await ctx.deal_damage(50, target=p)


card = PokemonCardDef(
    guid="fbacddd8-8b95-5fe4-9fc2-3745364f85c3",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=172,
    abilities=[
        Attack(
            title="Collateral Bolts",
            game_text="This attack does 50 damage to each Pokémon that has any damage counters on it (both yours and your opponent's), except for this Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=collateral_bolts,
        ),
        Attack(
            title="Electric Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
