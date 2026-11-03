"""Electabuzz (BWPJ 317 -- JP WAK 017; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="eb379655-b0d1-57d9-a165-278c633ca1ed",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic"],
    subtypes=["Basic"],
    collector_number=317,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=239,
    abilities=[
        Attack(
            title="Thunder Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
