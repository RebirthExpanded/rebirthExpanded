"""Venusaur & Snivy-GX (SM - Cosmic Eclipse 1/236 -- JP SM11a 001/064, the
art here).

Basic Grass TAG TEAM Pokemon-GX. HP 270, weakness Fire x2, retreat 3.

  Ability: Shining Vine  Once during your turn, if this Pokemon is your
                         Active Pokemon, when you attach a [G] Energy card
                         from your hand to it, you may switch 1 of your
                         opponent's Benched Pokemon with their Active
                         Pokemon.
  Forest Dump     [GCCC] 160
  Solar Plant-GX  [CCC+]  50 damage to each of your opponent's Pokemon. If
                  this Pokemon has at least 2 extra Energy attached to it
                  (in addition to this attack's cost), heal all damage from
                  all of your Pokemon.

Shining Vine is an ON_ENERGY_ATTACHED trigger: it goes off with the
attachment's other triggers (Rainbow Energy's damage counter) and this
Pokemon's owner orders them. With Mimikyu's Shadow Box in play, the
Rainbow counter first leaves it damaged and without Abilities, so Shining
Vine no longer goes off (official Q&A).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers
from spirit.game.session.legal_actions import attack_cost_satisfied
from spirit.game.session.passives import energy_provided_options

NAME = "Shining Vine"
_COST_PLUS_EXTRA = {"Colorless": 5}


def _grass_energy(board, energy) -> bool:
    return any(PokemonTypes.GRASS.value in option
               for option in energy_provided_options(board, energy))


def _shining_vine_applies(ctx) -> bool:
    """A [G] Energy card just attached from my hand to this Pokemon, my
    Active, during my turn; not used yet this turn; a Benched Pokemon to
    bring up."""
    me, energy = ctx.source, ctx.attached_energy
    if energy is None or ctx.energy_receiver is not me or energy.parent is not me:
        return False
    if ctx.attaching_player_id != ctx.player_id:
        return False
    state = ctx.session.turn_state
    if state.active_player_id != ctx.player_id or NAME in state.used_named_abilities:
        return False
    return (is_in_active_spot(me) and _grass_energy(ctx.board, energy)
            and bool(ctx.opponent_bench()))


async def shining_vine(ctx):
    if not _shining_vine_applies(ctx):
        return
    if not await ctx.ask_yes_no("Use Shining Vine to switch in 1 of your opponent's Benched Pokémon?"):
        return
    bench = ctx.opponent_bench()
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon to switch in") or bench[0]
    await ctx.switch_active(ctx.opponent_id, target)


async def solar_plant_gx(ctx):
    extra = attack_cost_satisfied(_COST_PLUS_EXTRA, ctx.attached_energies(ctx.attacker), ctx.board)
    await damage_all_opponents(50)(ctx)
    if extra:
        for pokemon in ctx.my_pokemon_in_play():
            await ctx.heal(9999, pokemon)


card = PokemonCardDef(
    guid="ac086c09-f040-5fd9-a795-3ca4f0465a98",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurSnivyGX.Name",
    display_name="Venusaur & Snivy-GX",
    searchable_by=["Venusaur & Snivy-GX", "Basic", "TAG TEAM", "GX", "VenusaurSnivyGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=1,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Ability(
            title=NAME,
            game_text="Once during your turn, if this Pokémon is your Active Pokémon, when you attach a [G] Energy card from your hand to it, you may switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=shining_vine,
            trigger_applies=_shining_vine_applies,
            shared_once_per_turn=NAME,
        ),
        Attack(
            title="Forest Dump",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
        Attack(
            title="Solar Plant-GX",
            game_text="This attack does 50 damage to each of your opponent's Pokémon. If this Pokémon has at least 2 extra Energy attached to it (in addition to this attack's cost), heal all damage from all of your Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=0,
            gx=True,
            effect=solar_plant_gx,
        ),
    ],
)
