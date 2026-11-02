"""Eevee V (Promo_SWSH 65 -- JP SD 075; English SP/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac



def _supporter_played(ctx) -> bool:
    return ctx.supporters_played_this_turn() > 0


card = PokemonCardDef(
    guid="7e5c748b-5c42-517b-a5b3-c9b5a9c5d8b5",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeV.Name",
    display_name="Eevee V",
    searchable_by=["Eevee V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=65,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(3),
        ),
        Attack(
            title="Brave Buddies",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_supporter_played, 80),
        ),
    ],
)
