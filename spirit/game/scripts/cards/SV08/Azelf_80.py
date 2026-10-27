"""Azelf (SV08 80 -- JP SV8 050; English SSP/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _all_opp_counters(ctx) -> int:
    return sum(_counters(ctx.board, p) for p in ctx.opponent_pokemon_in_play())


card = PokemonCardDef(
    guid="a0834e6d-1593-5345-ab4b-f5ebb4ce4b84",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name",
    display_name="Azelf",
    searchable_by=["Azelf", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=482,
    abilities=[
        Attack(
            title="Neurokinesis",
            game_text="This attack does 10 more damage for each damage counter on all of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_all_opp_counters, 10, base=10),
        ),
    ],
)
