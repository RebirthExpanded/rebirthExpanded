"""Gothita (BWPJ 322 -- JP WAK 022; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="117d3d20-2890-5b45-bea3-f81bd5c8140d",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    display_name="Gothita",
    searchable_by=["Gothita", "Basic"],
    subtypes=["Basic"],
    collector_number=322,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=574,
    abilities=[
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=10),
        ),
    ],
)
