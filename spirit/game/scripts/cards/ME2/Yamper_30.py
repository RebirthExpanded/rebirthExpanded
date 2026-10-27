"""Yamper (ME2 30 -- JP M2 030; English PFL/30, PFL/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3c9538f7-3d57-5a5b-b256-0504b5d1f956",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    display_name="Yamper",
    searchable_by=["Yamper", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=835,
    abilities=[
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
