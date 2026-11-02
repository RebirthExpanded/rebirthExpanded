"""Meowth V (Promo_SWSH 4 -- JP SP 028; English SP/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="8a8e5331-c2fe-5d41-9a1b-01710876f453",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeowthV.Name",
    display_name="Meowth V",
    searchable_by=["Meowth V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=4,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Pay Day",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Slashing Claw",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
