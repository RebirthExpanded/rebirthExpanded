"""Tadbulb (SV3 76 -- JP SV3 040; English OBF/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="76b7c935-efb6-5ae2-85c6-fe0bb73f308d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    display_name="Tadbulb",
    searchable_by=["Tadbulb", "Basic"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=938,
    abilities=[
        Attack(
            title="Shake and Discharge",
            game_text="This attack also does 10 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.snipe_attack(10, pool="bench", also_base=True),
        ),
    ],
)
