"""Bronzong (SV3 145 -- JP SV2P 051; English OBF/145). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


async def oracle_press(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, pc.attack_effect_shield_passive())


def _same_hands(ctx) -> bool:
    return len(ctx.hand()) == len(ctx.hand(ctx.opponent_id))


card = PokemonCardDef(
    guid="8951220d-f8d1-5e20-a6aa-fceaff0a297a",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Oracle Press",
            game_text="During your opponent's next turn, prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=oracle_press,
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_same_hands, 90),
        ),
    ],
)
