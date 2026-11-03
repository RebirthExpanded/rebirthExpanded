"""Sandile (BWPJ 331 -- JP WAK 031; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e37a272b-e36a-5ed2-ba29-32a2aa5ce761",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic"],
    subtypes=["Basic"],
    collector_number=331,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=551,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Continuous Pummel",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=30),
        ),
    ],
)
