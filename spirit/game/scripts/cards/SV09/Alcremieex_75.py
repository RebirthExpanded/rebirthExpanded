"""Alcremie ex (SV09 75 -- JP SVM 060; English JTG/75). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _any_hurt(board, player_id, pokemon) -> bool:
    return any(_counters(board, p) > 0 for p in board.pokemon_in_play(player_id))


async def confectionary_gift(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 30 damage from")
        if target is not None:
            await ctx.heal(30, target)


card = PokemonCardDef(
    guid="9e5f4b92-355f-5111-9d79-147896137e74",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremieex.Name",
    display_name="Alcremie ex",
    searchable_by=["Alcremie ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=75,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Ability(
            title="Confectionary Gift",
            game_text="Once during your turn, you may heal 30 damage from 1 of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_any_hurt,
            effect=confectionary_gift,
        ),
        Attack(
            title="Whipped Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
