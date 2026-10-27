"""Litten (SV05 32 -- JP SV5M 020; English TEF/167, TEF/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="25cc894a-0a72-5551-b5e8-619ad540418b",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    display_name="Litten",
    searchable_by=["Litten", "Basic"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=725,
    abilities=[
        Attack(
            title="Fake Out",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
