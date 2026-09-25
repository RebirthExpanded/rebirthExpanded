"""Necrozma (SM - Unified Minds 101/236 -- JP SM11 042/094).

Basic Psychic Pokemon. HP 130, weakness Psychic x2, retreat 2.

  Barrier Attack  [CC] 30    During your opponent's next turn, this Pokemon
                             takes 30 less damage from attacks (after
                             applying Weakness and Resistance).
  Special Laser   [PPC] 100+ If this Pokemon has any Special Energy attached
                             to it, this attack does 60 more damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import TakesLessPassive
from spirit.game.session.effects import is_special_energy
from spirit.game.data_utils import Attack, PokemonCardDef


async def barrier_attack(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TakesLessPassive(30))


def _has_special_energy(ctx) -> bool:
    return any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="5d390eaa-7889-5590-8bec-feb9ea572780",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Necrozma.Name",
    display_name="Necrozma",
    searchable_by=['Necrozma', 'Basic', 'Necrozma'],
    subtypes=['Basic'],
    collector_number=101,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Attack(title="Barrier Attack", game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
               cost={PokemonTypes.COLORLESS: 2}, damage=30,
               effect=barrier_attack),
        Attack(title="Special Laser", game_text="If this Pokémon has any Special Energy attached to it, this attack does 60 more damage.",
               cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=100, damage_operator="+",
               effect=bonus_if(_has_special_energy, 60)),
    ],
)
