"""Zangoose ex (ME2PT5 167 -- JP MC 588; English ASC/167). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8eebac25-c798-5fca-b8c7-ba1c47429ebb",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangooseex.Name",
    display_name="Zangoose ex",
    searchable_by=["Zangoose ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=167,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Wild Scissors",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=ac.recoil_attack(30),
        ),
    ],
)
