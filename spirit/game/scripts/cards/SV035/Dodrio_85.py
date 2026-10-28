"""Dodrio (SV035 85 -- JP SV2a 085; English MEW/85, PAF/200). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


def _defender_counters(ctx) -> int:
    return _counters(ctx.board, ctx.defender) if ctx.defender is not None else 0
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _zoom_condition(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and (pokemon.get_attribute(AttrID.HP, 0) or 0) > 10


async def zooming_draw(ctx):
    await ctx.deal_damage(10, target=ctx.source, apply_modifiers=False, as_counters=True)
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="7ae47bb1-a47b-5e77-81f4-d9b37f433f59",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Ability(
            title="Zooming Draw",
            game_text="Once during your turn, you may put 1 damage counter on this Pokémon. If you do, draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_zoom_condition,
            effect=zooming_draw,
        ),
        Attack(
            title="Ballistic Beak",
            game_text="This attack does 30 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_own, 30, base=10),
        ),
    ],
)
