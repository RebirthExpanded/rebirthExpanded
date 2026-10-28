"""Kingambit (SVP 130 -- JP SV3 082; English OBF/150, SVP/130). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def strike_down(ctx):
    d = ctx.opponent_active()
    if d is not None and not ctx.effects_blocked(d) and _counters(ctx.board, d) >= 4:
        await ctx.knock_out(d)


card = PokemonCardDef(
    guid="76740377-60b1-54b7-8f8e-ee8192fe3726",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingambit.Name",
    display_name="Kingambit",
    searchable_by=["Kingambit", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=130,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Strike Down",
            game_text="If your opponent's Active Pokémon has 4 or more damage counters on it, that Pokémon is Knocked Out.",
            cost={PokemonTypes.METAL: 1},
            effect=strike_down,
        ),
        Attack(
            title="Massive Rend",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
