"""Ting-Lu (SV4 109 -- JP SV4K 043; English PAR/109). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


async def _discard_to_one(ctx, pred, upto, label):
    pool = [c for c in ctx.discard_pile() if pred(c)]
    if not pool:
        return
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon")
    if target is None:
        return
    picks = await ctx.choose_cards(pool, min(upto, len(pool)), minimum=0, prompt=f"Attach up to {upto} {label}")
    for card in picks:
        await ctx.attach_energy(card, target)
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def sand_bringer(ctx):
    await _discard_to_one(ctx, _basic_fighting, 2, "Basic Fighting Energy cards")


async def arrogant_impact(ctx):
    if _counters(ctx.board, ctx.attacker) < 4:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="4167f195-fb7c-531e-899d-7792e2d105ea",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLu.Name",
    display_name="Ting-Lu",
    searchable_by=["Ting-Lu", "Basic"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=1003,
    abilities=[
        Attack(
            title="Sand Bringer",
            game_text="Attach up to 2 Basic Fighting Energy cards from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=sand_bringer,
        ),
        Attack(
            title="Arrogant Impact",
            game_text="If this Pokémon has 4 or more damage counters on it, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=220,
            effect=arrogant_impact,
        ),
    ],
)
