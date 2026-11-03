"""Golurk (BWPJ 46 -- JP BWP 046; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ab1c8fd1-f3c9-55a1-a7cf-edc8d3860bab",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Mega Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Dynamic Punch",
            game_text="Flip a coin. If heads, this attack does 30 more damage and your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=ac.condition_attack(SpecialConditions.CONFUSED, flip=True, heads_bonus_damage=30),
        ),
    ],
)
