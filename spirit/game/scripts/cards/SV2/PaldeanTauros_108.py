"""Paldean Tauros (SV2 108 -- JP SV1a 046; English PAF/172, PAL/108, PAL/218). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


def _defender_counters(ctx) -> int:
    return _counters(ctx.board, ctx.defender) if ctx.defender is not None else 0


card = PokemonCardDef(
    guid="35741517-2f0e-5365-a4af-86c2228915ae",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros", "Basic"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=128,
    abilities=[
        Attack(
            title="Raging Horns",
            game_text="This attack does 10 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(_own, 10, base=20),
        ),
        Attack(
            title="Combat Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.recoil_attack(30),
        ),
    ],
)
