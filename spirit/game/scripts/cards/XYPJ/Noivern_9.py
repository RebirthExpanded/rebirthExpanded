"""Noivern (XYPJ 9 -- JP XYP 009; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3d3ddcbd-e671-5616-b778-7d85bbfd2a77",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name",
    display_name="Noivern",
    searchable_by=["Noivern", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Wound Bite",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(ac.damage_counters_on("defender"), 10, base=20),
        ),
        Attack(
            title="Sonic Bazooka",
            game_text="Flip a coin. If heads, this attack does 30 more damage and your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.condition_attack(SpecialConditions.CONFUSED, flip=True, heads_bonus_damage=30),
        ),
    ],
)
