from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import subtypes_for
from spirit.game.card_effects.attacks_common import count_discard, damage_per


def _ancient(card) -> bool:
    return "Ancient" in subtypes_for(card.archetype_id)

card = PokemonCardDef(
    guid="78eef33b-3ea7-525f-9bb3-f367613e2fc3",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RoaringMoon.Name",
    display_name="Roaring Moon",
    searchable_by=["Roaring Moon", "Basic", "Ancient", "RoaringMoon"],
    subtypes=["Basic", "Ancient"],
    collector_number=109,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=1005,
    abilities=[
        Attack(
            title="Vengeance Fletching",
            game_text="This attack does 10 more damage for each Ancient card in your discard pile.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            damage_operator="+",
            effect=damage_per(count_discard("mine", _ancient), 10, base=70),
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)
