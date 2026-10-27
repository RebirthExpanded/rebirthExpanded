"""Tapu Koko (SV08 65 -- JP SV8 041; English SSP/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.session.effects import is_pokemon_card


def _lightning_mon(c) -> bool:
    return is_pokemon_card(c) and _of_type(c, PokemonTypes.LIGHTNING)


def _more_left(ctx) -> bool:
    return ac.count_prizes_remaining("mine")(ctx) > ac.count_prizes_remaining("opponent")(ctx)


card = PokemonCardDef(
    guid="dffe6ef3-bbfa-5e0a-958c-04ba42e86370",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKoko.Name",
    display_name="Tapu Koko",
    searchable_by=["Tapu Koko", "Basic"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Summon Lightning",
            game_text="Search your deck for up to 2 Lightning Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(_lightning_mon, count=2, reveal=True, prompt="Choose up to 2 Lightning Pokémon."),
        ),
        Attack(
            title="Prize Count",
            game_text="If you have more Prize cards remaining than your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_more_left, 90),
        ),
    ],
)
