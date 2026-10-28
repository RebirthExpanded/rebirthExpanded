"""Chansey (SV1 144 -- JP SV1V 059; English SVI/144). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="51af7d33-6a15-51d2-b701-968d7b395248",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=440,
    abilities=[
        Attack(
            title="Pound",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Egg Rolling",
            game_text="Flip a coin until you get tails. This attack does 60 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=60),
        ),
    ],
)
