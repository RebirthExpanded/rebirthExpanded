"""Machoke (SV035 67 -- JP SV2a 067; English MEW/177, MEW/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f3327fdf-7846-5e83-be5f-fb7ecc877b63",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Mountain Ramming",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            effect=ac.mill_attack(1),
        ),
    ],
)
