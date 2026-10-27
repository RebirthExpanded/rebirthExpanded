"""Trevenant (ME4 39 -- JP M4 039; English CRI/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def cursed_roots(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.restrict_attachments(defender)


def _opp_counters(ctx) -> int:
    return sum(_counters(ctx.board, p) for p in ctx.opponent_pokemon_in_play())


card = PokemonCardDef(
    guid="4f741b5e-1d4a-5462-a0d3-8c322e0e00e4",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Attack(
            title="Cursed Roots",
            game_text="During your opponent's next turn, Energy can't be attached from your opponent's hand to the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=cursed_roots,
        ),
        Attack(
            title="Overwhelming Pain",
            game_text="This attack does 10 more damage for each damage counter on all of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(_opp_counters, 10, base=60),
        ),
    ],
)
