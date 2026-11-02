"""Snivy (MEP 49 -- JP MP 113; English MEP/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="59ac188f-60d2-52f2-ad79-30437e576d31",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    display_name="Snivy",
    searchable_by=["Snivy", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=495,
    abilities=[
        Attack(
            title="Vine Whip",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
