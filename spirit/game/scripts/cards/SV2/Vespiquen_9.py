"""Vespiquen (SV2 9 -- JP SV2P 004; English PAL/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import full_stack


async def order_a_raid(ctx):
    pool = [p for p in ctx.my_bench() if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Combee"]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Combee to shuffle into your deck")
    if target is None:
        return
    await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="63bc99c6-61b2-5ca7-8c8a-c2617b0628d5",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Double Stab",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Order a Raid",
            game_text="Choose 1 of your Benched Combee and shuffle that Pokémon and all attached cards into your deck. If you can't shuffle a Combee into your deck, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=120,
            effect=order_a_raid,
        ),
    ],
)
