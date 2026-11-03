"""Volcanion (XYPJ 266 -- JP XYP 266; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9448627b-c636-5001-84fb-2b35ebaea4ea",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic"],
    subtypes=["Basic"],
    collector_number=266,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.recoil_attack(20),
        ),
    ],
)
