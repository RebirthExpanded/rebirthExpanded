"""Umbreon & Darkrai-GX (SM - Unified Minds 125/236 -- JP SM-M 010/031).

Basic Darkness TAG TEAM Pokemon-GX. HP 270, weakness Fighting x2,
resistance Psychic -20, retreat 2.

  Black Lance   [DDC] 150  This attack also does 60 damage to 1 of your
                           opponent's Benched Pokemon-GX or Pokemon-EX.
  Dead Moon-GX    [C]+     During your opponent's next turn, your opponent
                           can't play any Trainer cards from their hand. If
                           this Pokemon has at least 5 extra Darkness Energy
                           attached to it (in addition to this attack's
                           cost), your opponent's Active Pokemon is Knocked
                           Out.

Black Lance's snipe is picky about its target -- a Benched GX or EX, the
uppercase kind that Counter Energy and Electrode-GX also read -- so it is
the snipe factory with that filter rather than a free choice; with no legal
Benched target it deals its 150 and nothing else.

Dead Moon-GX knocks the Defending Pokemon out as an EFFECT, not damage, so
it goes through ctx.knock_out: it ignores HP entirely and an effect shield
(Latios-EX's Light Pulse, an Alolan Persian-GX) turns it off, which damage
prevention would not.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef, subtypes_for
from spirit.game.session.effects import is_trainer_card
from spirit.game.session.legal_actions import attack_cost_satisfied

# The [C] cost plus the five extra [D], asked as a single question.
_COST_PLUS_EXTRAS = {"Colorless": 1, "Darkness": 5}


def _is_gx_or_uppercase_ex(pokemon) -> bool:
    """"Pokemon-GX or Pokemon-EX": the SM/XY-era rule boxes, not SV's ex."""
    return any(s in ("GX", "EX") for s in subtypes_for(pokemon.archetype_id))


async def black_lance(ctx):
    """150, and 60 to a Benched GX or EX of theirs if they have one."""
    await ctx.deal_damage()
    targets = [p for p in ctx.opponent_bench() if _is_gx_or_uppercase_ex(p)]
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Benched Pokémon-GX or Pokémon-EX.")
    if target is None:
        target = targets[0]
    await ctx.deal_damage(60, target=target, apply_modifiers=False)


async def dead_moon_gx(ctx):
    """No Trainers from their hand next turn; with 5 extra [D], their
    Active is Knocked Out outright."""
    ctx.lock_plays(ctx.opponent_id, is_trainer_card)
    energies = ctx.attached_energies(ctx.attacker)
    if attack_cost_satisfied(_COST_PLUS_EXTRAS, energies, ctx.board):
        await ctx.knock_out(ctx.opponent_active())


card = PokemonCardDef(
    guid="9c7c8eeb-f8f5-598f-84c1-e3ee179b3e23",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonDarkraiGX.Name",
    display_name="Umbreon & Darkrai-GX",
    searchable_by=["Umbreon & Darkrai-GX", "Basic", "TAG TEAM", "GX",
                   "UmbreonDarkraiGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=125,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=197,
    abilities=[
        Attack(
            title="Black Lance",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon-GX or Pokémon-EX. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=black_lance,
        ),
        Attack(
            title="Dead Moon-GX",
            game_text="During your opponent's next turn, your opponent can't play any Trainer cards from their hand. If this Pokémon has at least 5 extra Darkness Energy attached to it (in addition to this attack's cost), your opponent's Active Pokémon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            gx=True,
            effect=dead_moon_gx,
        ),
    ],
)
