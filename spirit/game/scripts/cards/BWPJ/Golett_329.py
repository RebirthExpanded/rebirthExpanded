"""Golett (BWPJ 329 -- JP WAK 029; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="97739e00-d53f-5b3d-a111-e7a0a9ccb3fe",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett", "Basic"],
    subtypes=["Basic"],
    collector_number=329,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=622,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Mega Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
