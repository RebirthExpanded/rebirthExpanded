"""Electivire (SV05 54 -- JP SV5M 026; English TEF/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _opp_water(ctx) -> bool:
    return any(_of_type(p, PokemonTypes.WATER) for p in ctx.opponent_pokemon_in_play())


card = PokemonCardDef(
    guid="6ae443d4-f429-5e75-b32f-fdadc30cd44a",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=239,
    abilities=[
        Attack(
            title="Short-Circuit Knuckle",
            game_text="If your opponent has any Water Pokémon in play, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=ac.bonus_if(_opp_water, 120),
        ),
        Attack(
            title="Electroslug",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
