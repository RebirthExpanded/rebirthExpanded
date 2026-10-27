"""Baltoy (ME4 46 -- JP M4 046; English CRI/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b75ed06e-d7b8-573a-8aef-5ea4f968442b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    display_name="Baltoy",
    searchable_by=["Baltoy", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=343,
    abilities=[
        Attack(
            title="Continuous Spin",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=30),
        ),
    ],
)
