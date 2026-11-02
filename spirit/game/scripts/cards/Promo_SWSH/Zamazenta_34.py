"""Zamazenta (Promo_SWSH 34 -- JP SP1 004; English SP/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="dfc55dea-11db-5c98-8cec-e376f8a1d27e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name",
    display_name="Zamazenta",
    searchable_by=["Zamazenta", "Basic"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=889,
    abilities=[
        Ability(
            title="Sturdy Shield",
            game_text="This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(20),
        ),
        Attack(
            title="Headbang",
            game_text="",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
