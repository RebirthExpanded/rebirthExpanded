"""Deoxys V (Promo_SWSH 266 -- JP SPD 005; English SP/266). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f28cc3fb-bd30-532a-8ddb-5b371a80aea0",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name",
    display_name="Deoxys V",
    searchable_by=["Deoxys V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=266,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=386,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("opponent_active"), 30, base=30),
        ),
        Attack(
            title="Power Edge",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
