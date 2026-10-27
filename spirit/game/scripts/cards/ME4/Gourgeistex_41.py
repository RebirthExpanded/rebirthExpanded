"""Gourgeist ex (ME4 41 -- JP M4 041; English CRI/102, CRI/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _damaged_bench(ctx) -> int:
    return sum(1 for p in ctx.my_bench() if _counters(ctx.board, p) > 0)


async def ghostly_touch(ctx):
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id)


card = PokemonCardDef(
    guid="3f6f86c7-6c28-598b-a99c-c44a790c8e28",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeistex.Name",
    display_name="Gourgeist ex",
    searchable_by=["Gourgeist ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=41,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Attack(
            title="Horrifying Rondo",
            game_text="This attack does 50 more damage for each of your Benched Pokémon that has any damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(_damaged_bench, 50, base=30),
        ),
        Attack(
            title="Ghostly Touch",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=140,
            effect=ghostly_touch,
        ),
    ],
)
