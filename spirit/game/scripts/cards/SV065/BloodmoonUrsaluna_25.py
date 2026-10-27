"""Bloodmoon Ursaluna (SV065 25 -- JP SV6a 025; English PRE/54, SFA/25). Japanese art.
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
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


async def battle_hardened(ctx):
    if not getattr(ctx, "benched_from_hand", True):
        return
    pool = [c for c in ctx.hand() if _basic_fighting(c)]
    if not pool or not await ctx.ask_yes_no("Use Battle-Hardened?"):
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Fighting Energy cards to this Pokémon")
    for card in picks:
        await ctx.attach_energy(card, ctx.source)


card = PokemonCardDef(
    guid="c0e45d7b-8eb2-5fee-934c-e4af98cda358",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BloodmoonUrsaluna.Name",
    display_name="Bloodmoon Ursaluna",
    searchable_by=["Bloodmoon Ursaluna", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=216,
    abilities=[
        Ability(
            title="Battle-Hardened",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may attach up to 2 Basic Fighting Energy cards from your hand to this Pokémon.",
            trigger=Triggers.ON_PLAY,
            effect=battle_hardened,
        ),
        Attack(
            title="Mad Bite",
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.damage_per(_defender_counters, 30, base=100),
        ),
    ],
)
