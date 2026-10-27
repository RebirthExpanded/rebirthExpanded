"""Zeraora (MF 7 -- JP MF 007; English 30C/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6567e26d-c0c7-58fa-82ee-2a6936d19f46",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name",
    display_name="Zeraora",
    searchable_by=["Zeraora", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Rapid Draw",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Electrobullet",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.snipe_attack(20, pool="bench", also_base=True),
        ),
    ],
)
