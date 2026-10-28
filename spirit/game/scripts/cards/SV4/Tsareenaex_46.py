"""Tsareena ex (SV4 46 -- JP SV4K 020; English PAR/220, PAR/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES

_BY_NAME = {name: cond for cond, name in CLIENT_SPECIAL_CONDITION_NAMES.items()}


async def icicle_sole(ctx):
    pool = ctx.opponent_pokemon_in_play()
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon") if pool else None
    if target is None or ctx.effects_blocked(target):
        return
    hp = target.get_attribute(AttrID.HP, 0) or 0
    if hp > 30:
        await ctx.deal_damage(hp - 30, target=target, apply_modifiers=False, as_counters=True)


async def trop_kick(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    if me in ctx.knockouts:
        return
    await ctx.heal(30, me)
    for name in list(me.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        if name in _BY_NAME:
            await ctx.cure_condition(me, _BY_NAME[name])


card = PokemonCardDef(
    guid="7b4f5706-6ee3-562d-ad05-f2156d5de0c7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tsareenaex.Name",
    display_name="Tsareena ex",
    searchable_by=["Tsareena ex", "Stage 2", "ex", "Tera"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=46,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    family_id=761,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Icicle Sole",
            game_text="Put damage counters on 1 of your opponent's Pokémon until its remaining HP is 30.",
            cost={PokemonTypes.GRASS: 1},
            effect=icicle_sole,
        ),
        Attack(
            title="Trop Kick",
            game_text="Heal 30 damage from this Pokémon, and it recovers from all Special Conditions.",
            cost={PokemonTypes.GRASS: 2},
            damage=180,
            effect=trop_kick,
        ),
    ],
)
