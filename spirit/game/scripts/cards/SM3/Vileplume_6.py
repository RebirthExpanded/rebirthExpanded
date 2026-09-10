"""Vileplume (SM - Burning Shadows 6/147).

Stage 2 Grass Pokemon. HP 140, weakness Fire x2, no resistance, retreat 3.

  Ability  Disgusting Pollen  As long as this Pokemon is your Active
                              Pokemon, your opponent's Basic Pokemon can't
                              attack.

  Downer Shock [GGC] 60  Flip a coin. If heads, your opponent's Active
                         Pokemon is now Asleep. If tails, your opponent's
                         Active Pokemon is now Confused.

The pool's first continuous "can't attack" lock, so Passive gains
blocks_attacking and _attack_entries asks it before listing anything. The
per-attack refusals already had homes -- an Attack's own condition ("can't
attack unless you have 10 or more cards in your hand") and
TurnState.lock_attack for "during your next turn, this Pokemon can't
attack" -- and neither fits a rule that holds while a Pokemon sits across
the table.

Two conditions on the Ability, both from the text: this Vileplume must be
in the Active Spot, and only the opponent's BASIC Pokemon are stopped.
Since only the Active can attack anyway, in practice it stops their turn
whenever they are Active with a Basic.

The XY7 Vileplume in this pool is a different card with a different
Ability; this one shares only the name.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (AttrID, PokemonTypes, PokemonStage,
                                    Rarities, SpecialConditions)
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class DisgustingPollenPassive(Passive):
    """While this is Active, the opponent's Basic Pokemon cannot attack."""

    def blocks_attacking(self, pokemon, carrier):
        return (
            is_in_active_spot(carrier)
            and pokemon.owning_player_id != carrier.owning_player_id
            and pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        )


async def downer_shock(ctx):
    """60, then a coin: heads Asleep, tails Confused."""
    await ctx.deal_damage()
    heads, = await ctx.flip_coins(1, "Downer Shock")
    await ctx.apply_special_condition(
        ctx.defender,
        SpecialConditions.ASLEEP if heads else SpecialConditions.CONFUSED,
    )


card = PokemonCardDef(
    guid="b2519cd9-482f-5970-aab1-b7823203e4ec",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Disgusting Pollen",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Basic Pokémon can't attack.",
            passive=DisgustingPollenPassive(),
        ),
        Attack(
            title="Downer Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Asleep. If tails, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=downer_shock,
        ),
    ],
)
