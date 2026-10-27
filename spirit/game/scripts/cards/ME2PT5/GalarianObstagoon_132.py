"""Galarian Obstagoon (ME2PT5 132 -- JP M2a 107; English ASC/132, ASC/245). Japanese art.
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
    guid="9e2357e9-225a-5463-8da2-f62c9960be6a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name",
    display_name="Galarian Obstagoon",
    searchable_by=["Galarian Obstagoon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=132,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Scarring Shout",
            game_text="This attack does 70 damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=ac.damage_per(_defender_counters, 70),
        ),
        Attack(
            title="Punk Smash",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
