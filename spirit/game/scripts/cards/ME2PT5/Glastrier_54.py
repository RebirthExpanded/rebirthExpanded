"""Glastrier (ME2PT5 54 -- JP M2a 042; English ASC/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e45d67d7-0f45-555c-b38a-cac6c9daba03",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glastrier.Name",
    display_name="Glastrier",
    searchable_by=["Glastrier", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=896,
    abilities=[
        Attack(
            title="Ice Shot",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=ac.snipe_attack(20, pool="bench", also_base=True),
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="During your next turn, this Pokémon can't use Frosty Typhoon.",
            cost={PokemonTypes.WATER: 3},
            damage=130,
            locks_next_turn=True,
        ),
    ],
)
