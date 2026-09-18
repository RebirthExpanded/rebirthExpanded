"""Electrode-GX (SM - Celestial Storm 48/168 -- JP SM6b 022/066).

Stage 1 Lightning Pokemon-GX. HP 190, weakness Fighting x2, resistance
Metal -20, retreat 1.

  Ability  Extra Energy Bomb  Once during your turn (before your attack),
                              you may attach 5 Energy cards from your
                              discard pile to your Pokemon, except
                              Pokemon-GX and Pokemon-EX, in any way you
                              like. If you do, this Pokemon is Knocked Out.

  Electro Ball        [LC]  50
  Crush and Burn-GX   [LC]  30+  Discard any amount of Energy from your
                                 Pokemon. This attack does 50 more damage
                                 for each card discarded in this way.

Extra Energy Bomb pays for itself with the Pokemon: the Ability resolves,
then Electrode-GX is Knocked Out and the opponent takes 2 Prizes for it.
The Knock Out is part of the Ability, not damage, so it happens even at
full HP and no shield reads it as an attack.

"Except Pokemon-GX and Pokemon-EX" is the uppercase SM/XY exclusion this
pool already reads for Counter Energy: GX and the XY-era EX, not the
Scarlet & Violet lowercase "ex". Electrode-GX cannot feed itself either
way -- it is a GX -- so the Energy always lands on something else.

Crush and Burn-GX discards from YOUR POKEMON, any of them and any amount,
and counts CARDS discarded, so a Double Colorless is one card and 50 more
damage rather than two.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef, subtypes_for)
from spirit.game.session.effects import is_energy_card

MAX_ENERGY = 5
PER_CARD = 50


def _is_gx_or_uppercase_ex(pokemon) -> bool:
    """The SM/XY-era "Pokemon-GX and Pokemon-EX", not the SV lowercase ex."""
    return any(s in ("GX", "EX") for s in subtypes_for(pokemon.archetype_id))


def _bomb_targets(ctx):
    return [p for p in ctx.my_pokemon_in_play() if not _is_gx_or_uppercase_ex(p)]


def _bomb_condition(board, player_id, pokemon=None):
    """Energy in the discard, and something that is allowed to take it."""
    discard = board.find_player_area(player_id, "discard")
    if not any(is_energy_card(c) for c in (discard.children if discard else [])):
        return False
    return any(not _is_gx_or_uppercase_ex(p) for p in board.pokemon_in_play(player_id))


async def extra_energy_bomb(ctx):
    """Five Energy out of the discard onto anything but a GX or an EX --
    and then Electrode-GX goes with them."""
    energies = [c for c in ctx.discard_pile() if is_energy_card(c)]
    candidates = _bomb_targets(ctx)
    if not energies or not candidates:
        return
    picks = await ctx.choose_cards(
        energies, MAX_ENERGY, minimum=1,
        prompt="Choose Energy from your discard pile to attach.",
    )
    if not picks:
        return
    await distribute_energy(ctx, picks, candidates)
    await ctx.knock_out(ctx.source)


async def crush_and_burn_gx(ctx):
    """30 + 50 per Energy CARD discarded from anywhere on your side."""
    attached = [e for p in ctx.my_pokemon_in_play()
                for e in ctx.board.attached_energies(p)]
    discarded = []
    if attached:
        discarded = await ctx.choose_cards(
            attached, len(attached), minimum=0,
            prompt="Choose any amount of Energy to discard from your Pokémon.",
        )
        if discarded:
            await ctx.discard_cards(discarded)
    await ctx.deal_damage(30 + PER_CARD * len(discarded))


card = PokemonCardDef(
    guid="30244888-7aa1-57d5-8487-8f9fb34b4dcf",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrodegx.Name",
    display_name="Electrode-GX",
    searchable_by=["Electrode-GX", "Stage 1", "GX", "Electrodegx"],
    subtypes=["Stage 1", "GX"],
    collector_number=48,
    set_code="SM7",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Extra Energy Bomb",
            game_text="Once during your turn (before your attack), you may attach 5 Energy cards from your discard pile to your Pokémon, except Pokémon-GX and Pokémon-EX, in any way you like. If you do, this Pokémon is Knocked Out.",
            activation=Activations.ONCE_PER_TURN,
            condition=_bomb_condition,
            effect=extra_energy_bomb,
            self_knockout=True,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Crush and Burn-GX",
            game_text="Discard any amount of Energy from your Pokémon. This attack does 50 more damage for each card you discarded in this way. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            gx=True,
            effect=crush_and_burn_gx,
        ),
    ],
)
