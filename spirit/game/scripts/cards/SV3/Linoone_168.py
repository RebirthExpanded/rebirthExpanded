"""Linoone (SV3 168 -- JP SV3 093; English OBF/168). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3ecd768f-7199-5cd4-8405-69b777464bb3",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name",
    display_name="Linoone",
    searchable_by=["Linoone", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=168,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Jet Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=ac.recoil_attack(30),
        ),
    ],
)
