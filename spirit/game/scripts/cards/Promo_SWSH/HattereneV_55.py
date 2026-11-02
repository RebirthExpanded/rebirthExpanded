"""Hatterene V (Promo_SWSH 55 -- JP SP 111; English SP/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import support_common as su



async def _confuse_new_active(ctx, new_active):
    await ctx.apply_special_condition(new_active, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="fa29a2c1-4fcf-52eb-9670-6f16463d3deb",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HattereneV.Name",
    display_name="Hatterene V",
    searchable_by=["Hatterene V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=55,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=858,
    abilities=[
        Attack(
            title="Confounding Pulse",
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. The new Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=su.gust_then(_confuse_new_active),
        ),
        Attack(
            title="Mental Crush",
            game_text="If your opponent's Active Pokémon is Confused, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.CONFUSED), 90),
        ),
    ],
)
