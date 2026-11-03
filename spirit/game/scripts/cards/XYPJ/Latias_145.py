"""Latias (XYPJ 145 -- JP XYP 145; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="86f36a53-fea0-5c00-b84d-3abe4fd24ec1",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Attack(
            title="Psyshot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Psychic Prism",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
