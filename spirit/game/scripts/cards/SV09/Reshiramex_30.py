"""Reshiram ex (SV09 30 -- JP SVM 022; English JTG/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ac3ade61-fbfb-5d66-a08a-a74758bf71b3",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiramex.Name",
    display_name="Reshiram ex",
    searchable_by=["Reshiram ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=30,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Fire Wing",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
        ),
        Attack(
            title="Scorching Fire",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
