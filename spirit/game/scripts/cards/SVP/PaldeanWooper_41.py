"""Paldean Wooper (SVP 41 -- JP SV3 067; English SVP/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b4420747-2f61-5fbc-8ea6-91e0e6f3552b",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    display_name="Paldean Wooper",
    searchable_by=["Paldean Wooper", "Basic"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=194,
    abilities=[
        Attack(
            title="Splattering Poison",
            game_text="Both Active Pokémon are now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED, both_actives=True),
        ),
        Attack(
            title="Tail Whap",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
