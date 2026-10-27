"""Gurdurr (ZSV10PT5 48 -- JP SV11B 051; English BLK/126, BLK/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b55c5e2d-8094-5557-b726-1345e78aac71",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    display_name="Gurdurr",
    searchable_by=["Gurdurr", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ac.mill_attack(1),
        ),
    ],
)
