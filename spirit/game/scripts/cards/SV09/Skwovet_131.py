"""Skwovet (SV09 131 -- JP SVM 117; English JTG/131). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="3543a85e-0d13-5b81-b092-699896d20974",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    display_name="Skwovet",
    searchable_by=["Skwovet", "Basic"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
