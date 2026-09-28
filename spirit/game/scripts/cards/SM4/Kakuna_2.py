from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.support_common import search_to_bench


def _kakuna(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Kakuna"

card = PokemonCardDef(
    guid="70138cb2-7f28-5830-a2a6-e066392a1c46",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    display_name="Kakuna",
    searchable_by=["Kakuna", "Stage 1", "Kakuna"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Multiply",
            game_text="Search your deck for up to 3 Kakuna and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            damage=0,
            effect=search_to_bench(predicate=_kakuna, count=3, prompt="Choose up to 3 Kakuna to put onto your Bench."),
        ),
    ],
)
