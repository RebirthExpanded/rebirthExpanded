"""Zubat (SV4 110 -- JP SV4K 044; English PAR/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4ab00449-2158-5dac-892d-a36b69077f27",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat", "Basic"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=41,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Razor Wing",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
