"""Hoopa (XYPJ 155 -- JP XYP 155; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7e0c8069-990a-552b-9ebc-8a838af72d65",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name",
    display_name="Hoopa",
    searchable_by=["Hoopa", "Basic"],
    subtypes=["Basic"],
    collector_number=155,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Attack(
            title="Unbound Rush",
            game_text="Flip a coin for each of your Benched Pokémon. This attack does 30 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins_from=ac.count_bench("mine"), per_heads=30),
        ),
    ],
)
