"""Greedent (SV09 132 -- JP SVM 118; English JTG/132). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="47e6af4b-f011-5fc3-9bdc-7dc3edf39d45",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greedent.Name",
    display_name="Greedent",
    searchable_by=["Greedent", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=132,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    family_id=819,
    abilities=[
        Attack(
            title="Gluttonous Tail",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=su.draw_attack(2),
        ),
    ],
)
