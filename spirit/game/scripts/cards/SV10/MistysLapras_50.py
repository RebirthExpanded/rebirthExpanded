"""Misty's Lapras (SV10 50 -- JP SV9a 027; English DRI/194, DRI/50). Japanese art.
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

from spirit.game.session.effects import is_pokemon_card


def _mistys(card) -> bool:
    return is_pokemon_card(card) and _named("Misty's ")(card)


card = PokemonCardDef(
    guid="d1437369-57c0-5f42-a1f6-193851f31d13",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysLapras.Name",
    display_name="Misty's Lapras",
    searchable_by=["Misty's Lapras", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Swim Together",
            game_text="Search your deck for up to 3 Misty's Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=su.search_to_hand(_mistys, count=3, reveal=True, prompt="Choose up to 3 Misty's Pokémon."),
        ),
        Attack(
            title="Surf",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
