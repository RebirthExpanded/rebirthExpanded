"""Beheeyem (ZSV10PT5 41 -- JP SV11B 044; English BLK/121, BLK/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2035f927-1fd7-57ab-a496-f78fb8401e46",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    display_name="Beheeyem",
    searchable_by=["Beheeyem", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    family_id=605,
    abilities=[
        Attack(
            title="Calm Mind",
            game_text="Heal 40 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.heal_attack(40),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 30, base=80),
        ),
    ],
)
