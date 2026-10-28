"""Stonjourner (SV1 121 -- JP SVAM 010; English SVI/121). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="3e4f2d90-7d90-54e5-8c49-746c6b00d2da",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name",
    display_name="Stonjourner",
    searchable_by=["Stonjourner", "Basic"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(20),
        ),
        Attack(
            title="Mega Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
