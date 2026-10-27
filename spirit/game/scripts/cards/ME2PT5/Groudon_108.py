"""Groudon (ME2PT5 108 -- JP MC 375; English ASC/108). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8630e65d-309b-5d0f-9406-f52799b288ed",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
        Attack(
            title="Megaton Fall",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=ac.recoil_attack(30),
        ),
    ],
)
