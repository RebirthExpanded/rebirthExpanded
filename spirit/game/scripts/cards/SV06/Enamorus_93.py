"""Enamorus (SV06 93 -- JP SV5a 039; English TWM/180, TWM/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _types(p):
    return set(p.get_attribute(AttrID.POKEMON_TYPES) or [])


def _shared_type(ctx) -> bool:
    mine = set().union(*[_types(p) for p in ctx.my_pokemon_in_play()]) if ctx.my_pokemon_in_play() else set()
    theirs = set().union(*[_types(p) for p in ctx.opponent_pokemon_in_play()]) if ctx.opponent_pokemon_in_play() else set()
    return bool(mine & theirs)


card = PokemonCardDef(
    guid="f77b8b46-b6ff-5845-9f8e-40d790939d95",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Enamorus.Name",
    display_name="Enamorus",
    searchable_by=["Enamorus", "Basic"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=905,
    abilities=[
        Attack(
            title="Heart Sign",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Love Resonance",
            game_text="If any of your Pokémon in play are the same type as any of your opponent's Pokémon in play, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_shared_type, 120),
        ),
    ],
)
