"""Team Rocket's Koffing (SV10 125 -- JP SV10 069; English DRI/125). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import passives_common as pc
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


def _koffing(card) -> bool:
    return is_pokemon_card(card) and _name_has("Koffing")(card)


card = PokemonCardDef(
    guid="4d9a6e14-79d0-5434-bf40-e6c73335c58c",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsKoffing.Name",
    display_name="Team Rocket's Koffing",
    searchable_by=["Team Rocket's Koffing", "Basic"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=109,
    abilities=[
        Ability(
            title="Smog Signals",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), search your deck for up to 2 Pokémon that have \"Koffing\" in their name and put them onto your Bench. Then, shuffle your deck.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=su.search_to_bench(_koffing, count=2, prompt="Choose up to 2 Pokémon that have Koffing in their name."),
        ),
        Attack(
            title="Leaking Gas",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
