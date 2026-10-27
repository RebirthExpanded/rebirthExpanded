"""Celebi (SV07 4 -- JP SVI 001; English SCR/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="4cfdd0ab-ef63-52cb-a9ae-0f65900d5cfd",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Leaf Step",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
