"""Meowth VMAX (Promo_SWSH 5 -- JP SP 029; English SP/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="678e4193-f0da-581e-94b7-3852ecf3483a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeowthVMAX.Name",
    display_name="Meowth VMAX",
    searchable_by=["Meowth VMAX", "VMAX"],
    subtypes=["VMAX"],
    collector_number=5,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MeowthV.Name",
    family_id=52,
    abilities=[
        Attack(
            title="G-Max Gold Rush",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=su.draw_attack(3),
        ),
    ],
)
