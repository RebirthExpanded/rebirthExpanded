"""Garbodor (RSV10PT5 60 -- JP SV11W 057; English WHT/141, WHT/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="538b54d4-0d64-5d6f-9487-88e21dc43d04",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Attack(
            title="Suffocating Gas",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Gunk Shot",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
