from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.support_common import search_to_bench


def _lampent(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Lampent"

card = PokemonCardDef(
    guid="352a22cf-bb92-5159-81e3-67b32a65437e",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Spreading Light",
            game_text="Search your deck for up to 3 Lampent and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=0,
            effect=search_to_bench(predicate=_lampent, count=3, prompt="Choose up to 3 Lampent to put onto your Bench."),
        ),
    ],
)
