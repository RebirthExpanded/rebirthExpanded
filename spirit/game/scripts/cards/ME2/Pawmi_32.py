"""Pawmi (ME2 32 -- JP M2 032; English PFL/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="3c6c27f9-9fb3-535e-a098-ff91501fe658",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    display_name="Pawmi",
    searchable_by=["Pawmi", "Basic"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=921,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=pc.debuff_defender_attacks(30),
        ),
        Attack(
            title="Tiny Charge",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
