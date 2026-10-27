"""Electrike (ME1 49 -- JP M1S 031; English MEG/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ef239e9b-64d6-5145-a99c-91850ca045f7",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=309,
    abilities=[
        Attack(
            title="Thunder Jolt",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
