"""Wobbuffet (SMD 8 -- JP SMD 008; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6170d325-7e01-5840-a114-e68dba4eb6e9",
    key="SMD",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SMD",
    regulation_mark="A",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=360,
    abilities=[
        Attack(
            title="Party Attack",
            game_text="Flip a coin for each of your Pokémon in play. This attack does 30 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins_from=ac.count_in_play("mine"), per_heads=30),
        ),
    ],
)
