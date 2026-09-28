from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.support_common import remove_self_from_play, search_to_bench


def _is_lillies(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Lillie's ")


def _basic_lillies(card) -> bool:
    return is_basic_pokemon(card) and _is_lillies(card)

card = PokemonCardDef(
    guid="26cb19c0-07d7-5107-aa9a-3572fc1df269",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesComfey.Name",
    display_name="Lillie's Comfey",
    searchable_by=["Lillie's Comfey", "Basic", "LilliesComfey"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=764,
    abilities=[
        Attack(
            title="Inviting Flowers",
            game_text="You may search your deck for any number of Basic Lillie's Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=search_to_bench(predicate=_basic_lillies, count=8, prompt="Choose any number of Basic Lillie's Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Fade Out",
            game_text="Put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=remove_self_from_play("hand"),
        ),
    ],
)
