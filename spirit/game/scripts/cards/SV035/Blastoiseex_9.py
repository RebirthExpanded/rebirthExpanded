"""Blastoise ex (SV035 9 -- JP SV2a 009; English MEW/184, MEW/200, MEW/9, SCR/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


async def twin_cannons(ctx):
    pool = [c for c in ctx.hand() if _basic_water(c)]
    if not pool:
        return
    picks = await ctx.discard_from_hand(min(2, len(pool)), minimum=0, predicate=_basic_water,
                                        prompt="Discard up to 2 Basic Water Energy cards from your hand")
    if picks:
        await ctx.deal_damage(140 * len(picks))


card = PokemonCardDef(
    guid="0da11543-6597-5c66-afe6-b1102e149498",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoiseex.Name",
    display_name="Blastoise ex",
    searchable_by=["Blastoise ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=9,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30),
        ),
        Attack(
            title="Twin Cannons",
            game_text="Discard up to 2 Basic Water Energy cards from your hand. This attack does 140 damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=140,
            damage_operator="x",
            effect=twin_cannons,
        ),
    ],
)
