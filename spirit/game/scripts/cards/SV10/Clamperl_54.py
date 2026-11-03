"""Clamperl (SV10 54 -- JP SV10 023; English DRI/195, DRI/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="5cef305e-fcd0-5f86-8248-0d50ce8302f0",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    display_name="Clamperl",
    searchable_by=["Clamperl", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=366,
    abilities=[
        Attack(
            title="Shell Press",
            game_text="During your opponent's next turn, this Pokémon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=pc.protect_next_turn(reduce=10),
        ),
    ],
)
