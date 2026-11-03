"""Blitzle (BWPJ 405 -- JP CS1 005; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="43ceb343-db45-54eb-87b9-356db66b417b",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    display_name="Blitzle",
    searchable_by=["Blitzle", "Basic"],
    subtypes=["Basic"],
    collector_number=405,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=522,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
