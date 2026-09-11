"""Dialga-EX (JP XY Hyper Metal Chain Deck 60 -- HMC 004/018; English print
XY - Phantom Forces 62/119).

Basic Metal Pokemon-EX. HP 180, weakness Fire x2, resistance Psychic -20,
retreat 2.

  Chrono Wind        [MCC] 60   If the Defending Pokemon is a Pokemon-EX,
                                it can't attack during your opponent's
                                next turn.
  Full Metal Impact  [MMCC] 150  Discard 2 [M] Energy attached to this
                                 Pokemon.

Pokemon-EX is the uppercase rule box: a Scarlet & Violet ex is not locked.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import (lock_defender_attacks,
                                                     self_energy_discard_attack)
from spirit.game.data_utils import Attack, PokemonCardDef, subtypes_for


async def chrono_wind(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and "EX" in subtypes_for(defender.archetype_id):
        lock_defender_attacks(ctx, defender)


card = PokemonCardDef(
    guid="cc6aca03-3c50-5f7f-8302-a46b1612ffae",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaEX.Name",
    display_name="Dialga-EX",
    searchable_by=["Dialga-EX", "Basic", "EX", "DialgaEX"],
    subtypes=["Basic", "EX"],
    collector_number=4,
    set_code="HMC",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=483,
    abilities=[
        Attack(
            title="Chrono Wind",
            game_text="If the Defending Pokémon is a Pokémon-EX, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=chrono_wind,
        ),
        Attack(
            title="Full Metal Impact",
            game_text="Discard 2 [M] Energy attached to this Pokémon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.METAL),
        ),
    ],
)
