"""Flapple (SV08 139 -- JP SV7a 046; English SSP/139, SSP/210). Japanese art.
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
    guid="80fab1cc-2284-5ef9-b8b9-326e4ecaba12",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flapple.Name",
    display_name="Flapple",
    searchable_by=["Flapple", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=139,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Acidic Spit",
            game_text="This attack does 20 damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_defender_counters, 20),
        ),
        Attack(
            title="Speed Dive",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=70,
        ),
    ],
)
