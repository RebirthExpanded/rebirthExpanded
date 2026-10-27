"""Mega Scrafty ex (ME2PT5 135 -- JP M2a 110; English ASC/135, ASC/270, ASC/285). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


def _revenge(n):
    async def effect(ctx):
        attacker = ctx.damaged_by
        if attacker is not None:
            await ctx.deal_damage(10 * n, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)
    return effect


async def outlaw_leg(ctx):
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)
    top = list(ctx.deck_top(1, player_id=ctx.opponent_id))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="44544cec-6796-5c8e-b779-db98f7855588",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaScraftyex.Name",
    display_name="Mega Scrafty ex",
    searchable_by=["Mega Scrafty ex", "Stage 1", "ex", "SV_Mega"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=135,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Ability(
            title="Counterattacking Crest",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), place 5 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=_revenge(5),
        ),
        Attack(
            title="Outlaw Leg",
            game_text="Discard a random card from your opponent's hand. Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=outlaw_leg,
        ),
    ],
)
