"""Charjabug (SV05 55 -- JP SV5M 027; English ASC/65, TEF/169, TEF/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="85dd9871-8a26-5f0e-82eb-a546a7795348",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    display_name="Charjabug",
    searchable_by=["Charjabug", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Static Shock",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
        ),
    ],
)
