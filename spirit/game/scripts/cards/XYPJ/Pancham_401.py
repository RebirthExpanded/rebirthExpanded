"""Pancham (XYPJ 401 -- JP XYC 001; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="75960fd0-af43-5639-98a4-53acdfc5aa05",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    display_name="Pancham",
    searchable_by=["Pancham", "Basic"],
    subtypes=["Basic"],
    collector_number=401,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=674,
    abilities=[
        Attack(
            title="Wallop",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(10),
        ),
    ],
)
