"""Pikachu ex (SV085 28 -- JP SVM 038; English PRE/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="48e4a8b9-36eb-5c6d-9709-0a98f00e118a",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=28,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Tail Whap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Thunder",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=ac.recoil_attack(30),
        ),
    ],
)
