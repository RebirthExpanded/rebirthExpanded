"""Scorbunny (ME1 26 -- JP M1L 015; English MEG/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0afd338b-d8ad-56a6-8ce0-588a6462f7f7",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    display_name="Scorbunny",
    searchable_by=["Scorbunny", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=813,
    abilities=[
        Attack(
            title="Wild Kick",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
