"""Tyranitar ex (SV3 66 -- JP SV3 032; English OBF/211, OBF/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def mountain_hurl(ctx):
    await ctx.deal_damage()
    top = list(ctx.deck_top(2))
    if top:
        await ctx.discard_cards(top)


def _bench_damaged(ctx) -> bool:
    return any(_counters(ctx.board, p) > 0 for p in ctx.my_bench())


card = PokemonCardDef(
    guid="ac9f894c-467f-5f5c-b715-342f16c94ba4",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitarex.Name",
    display_name="Tyranitar ex",
    searchable_by=["Tyranitar ex", "Stage 2", "ex", "Tera"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=66,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Mountain Hurl",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=120,
            effect=mountain_hurl,
        ),
        Attack(
            title="Lightning Rampage",
            game_text="If your Benched Pokémon have any damage counters on them, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=150,
            damage_operator="+",
            effect=ac.bonus_if(_bench_damaged, 100),
        ),
    ],
)
