"""Bouffalant (SV3 174 -- JP SVD 098; English OBF/174). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5e2a8c4c-34e5-55ac-9791-87a779fea39e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic"],
    subtypes=["Basic"],
    collector_number=174,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Ability(
            title="Bouffer",
            game_text="This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(20),
        ),
        Attack(
            title="Damage Rush",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=ac.flip_damage(until_tails=True, bonus_per_heads=30),
        ),
    ],
)
