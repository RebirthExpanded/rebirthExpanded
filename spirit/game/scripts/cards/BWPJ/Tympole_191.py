"""Tympole (BWPJ 191 -- JP BWP 191; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0df1e42f-ce30-51af-9473-b3d0e3dc30fc",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    display_name="Tympole",
    searchable_by=["Tympole", "Basic"],
    subtypes=["Basic"],
    collector_number=191,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=535,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Resonance",
            game_text="If your opponent's Active Pokémon is Confused, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.condition_bonus_attack(20, SpecialConditions.CONFUSED),
        ),
    ],
)
