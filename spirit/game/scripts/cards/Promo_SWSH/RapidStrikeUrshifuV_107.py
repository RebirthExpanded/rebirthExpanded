"""Rapid Strike Urshifu V (Promo_SWSH 107 -- JP SF 007; English SP/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d78e2c88-88b3-5f03-a79b-ed9383bf8c46",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifuV.Name",
    display_name="Rapid Strike Urshifu V",
    searchable_by=["Rapid Strike Urshifu V", "Basic", "V", "Rapid Strike"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=107,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=892,
    abilities=[
        Attack(
            title="Spiral Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Sonic Legs",
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=ac.snipe_attack(20, pool="bench", count=2, also_base=True),
        ),
    ],
)
