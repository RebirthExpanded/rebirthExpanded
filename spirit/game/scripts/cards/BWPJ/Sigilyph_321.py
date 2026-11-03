"""Sigilyph (BWPJ 321 -- JP WAK 021; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c65ac9e3-78f8-5f0a-867e-ef9ad49bd48b",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic"],
    subtypes=["Basic"],
    collector_number=321,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=561,
    abilities=[
        Attack(
            title="Ambush",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
