"""Vanillite (RSV10PT5 27 -- JP SV11W 024; English WHT/111, WHT/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="da8b6e8a-411f-528c-a08c-76475f0f383d",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    display_name="Vanillite",
    searchable_by=["Vanillite", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=582,
    abilities=[
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Ice Edge",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
