"""Heatmor (BWPJ 309 -- JP WAK 009; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6cc94c4b-aacb-5661-90bc-065631d97ea3",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic"],
    subtypes=["Basic"],
    collector_number=309,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Live Coal",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
        Attack(
            title="Heat Blast",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
