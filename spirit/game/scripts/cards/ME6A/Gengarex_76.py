"""Gengar ex (JP M6a 076/103 -- 30th Celebrations; English 30C 90).
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers


async def fainting_spell(ctx):
    """KO'd by the opponent's attack damage: flip; heads KOs the attacker."""
    attacker = getattr(ctx, "ko_attacker", None)
    if not getattr(ctx, "ko_from_attack", False) or attacker is None:
        return
    if (await ctx.flip_coins(1, "Fainting Spell"))[0]:
        await ctx.knock_out(attacker)


async def chaotic_pain(ctx):
    """13 damage counters on 1 of the opponent's Pokemon."""
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon for 13 damage counters")
    if target is not None:
        await ctx.deal_damage(130, target=target, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="354a6f1e-c067-5ef4-a3a0-34b0af21b978",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengarex.Name",
    display_name="Gengar ex",
    searchable_by=["Gengar ex", "Stage 2", "ex", "Gengarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=76,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Fainting Spell",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, flip a coin. If heads, the Attacking Pok\u00e9mon is Knocked Out.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=fainting_spell,
            trigger_applies=lambda c: bool(c.ko_from_attack),
        ),
        Attack(
            title="Chaotic Pain",
            game_text="Place 13 damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=0,
            effect=chaotic_pain,
        ),
    ],
)
