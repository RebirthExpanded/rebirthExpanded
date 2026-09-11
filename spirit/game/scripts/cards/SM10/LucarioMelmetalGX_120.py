"""Lucario & Melmetal-GX (SM - Unbroken Bonds 120/214 -- JP SM9b 029/054).

Basic Metal TAG TEAM Pokemon-GX. HP 260, weakness Fire x2, resistance
Psychic -20, retreat 3.

  Steel Fist          [CC]   50  Search your deck for a Metal Energy card
                                 and attach it to this Pokemon. Then,
                                 shuffle your deck.
  Heavy Impact        [MMCC] 150
  Full Metal Wall-GX  [C]        For the rest of this game, your Metal
                                 Pokemon take 30 less damage from your
                                 opponent's attacks (after applying Weakness
                                 and Resistance). With 1 extra Energy
                                 attached, discard all Energy from your
                                 opponent's Active Pokemon.

"For the rest of this game" is the pool's first effect that outlives its
own card, so it needed somewhere to live: board.game_passives holds
(passive, owner) pairs that _collect_passives adds to every board read.
Nothing switches them off -- not an Ability lock, not the GX leaving play,
not a new Stadium -- and nothing prunes them at a turn boundary.

The passive itself is the ordinary takes-less shape with two filters: the
protected Pokemon must be a Metal Pokemon and must belong to the player
who used the attack, which the passive remembers because its carrier is
only an anchor.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import is_metal_energy
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.legal_actions import attack_cost_satisfied
from spirit.game.session.passives import Passive

REDUCTION = 30
# The [C] cost plus the one extra Energy, asked as a single question.
_COST_PLUS_EXTRA = {"Colorless": 2}


class FullMetalWallPassive(Passive):
    """Game-long: this player's Metal Pokemon take 30 less from opposing
    attacks. Player-scoped, so the carrier it is handed is only an anchor."""

    def __init__(self, player_id: str):
        self.player_id = player_id

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        target = calc.target
        if target is None or target.owning_player_id != self.player_id:
            return
        if not is_pokemon_of_type(target, PokemonTypes.METAL):
            return
        if "full_metal_wall" in calc.applied_once:
            return
        calc.applied_once.add("full_metal_wall")
        calc.amount = max(0, calc.amount - REDUCTION)


async def full_metal_wall_gx(ctx):
    """The wall goes up for good; an extra Energy strips their Active."""
    ctx.add_game_passive(FullMetalWallPassive(ctx.player_id))
    energies = ctx.attached_energies(ctx.attacker)
    if not attack_cost_satisfied(_COST_PLUS_EXTRA, energies, ctx.board):
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 99, prompt="Discard all Energy from the Defending Pokémon")


card = PokemonCardDef(
    guid="b208b92b-c043-5af7-9ad6-18cbe627a41e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioMelmetalGX.Name",
    display_name="Lucario & Melmetal-GX",
    searchable_by=["Lucario & Melmetal-GX", "Basic", "TAG TEAM", "GX",
                   "LucarioMelmetalGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=120,
    set_code="SM10",
    rarity=Rarities.RareHoloGX,
    hp=260,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=448,
    abilities=[
        Attack(
            title="Steel Fist",
            game_text="Search your deck for a Metal Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=search_attach_energy(predicate=is_metal_energy, count=1,
                                        to_self=True),
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
        ),
        Attack(
            title="Full Metal Wall-GX",
            game_text="For the rest of this game, your Metal Pokémon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance). If this Pokémon has at least 1 extra Energy attached to it (in addition to this attack's cost), discard all Energy from your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            gx=True,
            effect=full_metal_wall_gx,
        ),
    ],
)
