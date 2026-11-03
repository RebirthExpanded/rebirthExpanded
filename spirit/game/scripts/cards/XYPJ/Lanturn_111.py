"""Lanturn (XYPJ 111 -- JP XYP 111; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="29418706-4970-50e3-bfaa-f55f245ef317",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Attack(
            title="Drain Fin",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Light Wave",
            game_text="Discard an Energy from this Pokémon. Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=ac.self_energy_discard_attack(1, also=ac.condition_attack(SpecialConditions.CONFUSED, damage=0)),
        ),
    ],
)
