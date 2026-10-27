"""Steven's Baltoy (SV10 83 -- JP SVOD 001; English DRI/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import def_for, subtypes_for


def _named(prefix):
    def pred(card) -> bool:
        return card is not None and (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith(prefix)
    return pred


def _name_has(*parts):
    def pred(card) -> bool:
        name = (getattr(def_for(card.archetype_id), "display_name", "") or "") if card is not None else ""
        return any(p in name for p in parts)
    return pred

from spirit.game.session.effects import is_basic_pokemon


def _basic_steven(card) -> bool:
    return is_basic_pokemon(card) and _named("Steven's ")(card)


card = PokemonCardDef(
    guid="7f4e6672-ab74-5600-861c-a677617ac614",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBaltoy.Name",
    display_name="Steven's Baltoy",
    searchable_by=["Steven's Baltoy", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=343,
    abilities=[
        Attack(
            title="Summoning Sign",
            game_text="Search your deck for up to 2 Basic Steven's Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(_basic_steven, count=2, prompt="Choose up to 2 Basic Steven's Pokémon."),
        ),
        Attack(
            title="Psychic Sphere",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
