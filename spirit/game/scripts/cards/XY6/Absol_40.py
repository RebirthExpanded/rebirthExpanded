"""Absol (XY - Roaring Skies 40/108 -- JP XY6-B 034/078, the art here).

Basic Darkness Pokemon. HP 100, weakness Fighting x2, resistance Psychic
-20, retreat 1.

  Ability: Cursed Eyes  When you play this Pokemon from your hand onto
                        your Bench, you may move 3 damage counters from 1
                        of your opponent's Pokemon to another of his or her
                        Pokemon.
  Mach Claw [DC] 30  This attack's damage isn't affected by Resistance.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers
from spirit.game.session.passives import moving_damage_counters_blocked

COUNTERS = 3


def _damaged(ctx):
    return [p for p in ctx.opponent_pokemon_in_play()
            if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]


def _cursed_eyes_applies(ctx) -> bool:
    return bool(_damaged(ctx)) and len(ctx.opponent_pokemon_in_play()) > 1


async def cursed_eyes(ctx):
    if not _cursed_eyes_applies(ctx):
        return
    if not await ctx.ask_yes_no("Use Cursed Eyes to move 3 damage counters?"):
        return
    source = await ctx.choose_pokemon(
        _damaged(ctx), "Choose 1 of your opponent's Pokémon to move damage counters from")
    if source is None:
        return
    if moving_damage_counters_blocked(ctx.board, source):
        await ctx.remove_damage_counters(source, COUNTERS)
        return
    targets = [p for p in ctx.opponent_pokemon_in_play() if p is not source]
    dest = await ctx.choose_pokemon(
        targets, "Choose a Pokémon to move the damage counters to")
    if dest is not None:
        await ctx.move_damage_counters(source, dest, max_count=COUNTERS)


async def mach_claw(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="95af9472-0d80-5c77-951b-9e4e0095b01e",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=359,
    abilities=[
        Ability(
            title="Cursed Eyes",
            game_text="When you play this Pokémon from your hand onto your Bench, you may move 3 damage counters from 1 of your opponent's Pokémon to another of his or her Pokémon.",
            trigger=Triggers.ON_PLAY,
            effect=cursed_eyes,
            trigger_applies=_cursed_eyes_applies,
        ),
        Attack(
            title="Mach Claw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=mach_claw,
        ),
    ],
)
