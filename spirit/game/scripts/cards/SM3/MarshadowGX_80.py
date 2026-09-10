"""Marshadow-GX (SM - Burning Shadows 80/147 -- JP SM8b 064/150).

Basic Fighting Pokemon-GX. HP 150, weakness Psychic x2, retreat 1.

  Ability  Shadow Hunt  This Pokemon can use the attacks of any Basic
                        Pokemon in your discard pile. (You still need the
                        necessary Energy to use each attack.)

  Beatdown                    [FFC] 120
  Peerless Hundred Blows-GX    [F]  50x  This attack does 50 damage times
                                         the number of basic Energy attached
                                         to this Pokemon.

Shadow Hunt is Ditto's Sudden Transformation without the Rule Box
exclusion -- it is older text, and every Basic in the discard is fair game,
GX and EX included. Both now sit on the shared borrowed-attacks passive.

Peerless Hundred Blows-GX counts basic Energy CARDS attached here, so a
Double Colorless or a Rainbow adds nothing to it however much Energy it
provides.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.pokemon import (BorrowedAttacksPassive,
                                              own_discard_cards)
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_basic_energy, is_basic_pokemon

PER_ENERGY = 50


def _count_basic_energy(ctx) -> int:
    return sum(1 for e in ctx.attached_energies(ctx.attacker) if is_basic_energy(e))


card = PokemonCardDef(
    guid="e9192429-f76a-5269-b55a-4f31a45a3495",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarshadowGX.Name",
    display_name="Marshadow-GX",
    searchable_by=["Marshadow-GX", "Basic", "GX", "MarshadowGX"],
    subtypes=["Basic", "GX"],
    collector_number=80,
    set_code="SM3",
    rarity=Rarities.RareHoloGX,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=802,
    abilities=[
        Ability(
            title="Shadow Hunt",
            game_text="This Pokémon can use the attacks of any Basic Pokémon in your discard pile. (You still need the necessary Energy to use each attack.)",
            passive=BorrowedAttacksPassive(own_discard_cards, is_basic_pokemon),
        ),
        Attack(
            title="Beatdown",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Peerless Hundred Blows-GX",
            game_text="This attack does 50 damage times the number of basic Energy attached to this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            gx=True,
            effect=damage_per(_count_basic_energy, PER_ENERGY),
        ),
    ],
)
