"""Sandshrew (SV06 97 -- JP SV6 057; English TWM/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="605f97c3-3182-523c-bc04-3c258982a385",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    display_name="Sandshrew",
    searchable_by=["Sandshrew", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=27,
    abilities=[
        Attack(
            title="Rollout",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=20),
        ),
    ],
)
