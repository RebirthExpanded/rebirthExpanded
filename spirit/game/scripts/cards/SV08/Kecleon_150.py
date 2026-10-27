"""Kecleon (SV08 150 -- JP SV8 086; English SSP/150, SSP/213). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="17b7be1d-f6e2-51b9-8ee7-80e9f459b76e",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic"],
    subtypes=["Basic"],
    collector_number=150,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Expert Hider",
            game_text="If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.",
            passive=pc.flip_prevent_damage_passive("Expert Hider"),
        ),
        Attack(
            title="Lick Whip",
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=ac.snipe_attack(30, pool="any"),
        ),
    ],
)
