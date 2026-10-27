"""Scovillain ex (SV08 37 -- JP SV8 023; English SSP/216, SSP/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


def _defender_counters(ctx) -> int:
    return _counters(ctx.board, ctx.defender) if ctx.defender is not None else 0



class DoubleTypePassive(Passive):
    """In play: Grass and Fire type."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return types
        return [PokemonTypes.GRASS.value, PokemonTypes.FIRE.value]


card = PokemonCardDef(
    guid="6b55c90e-fc2e-54d2-aa73-8d4ef85ce1c9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillainex.Name",
    display_name="Scovillain ex",
    searchable_by=["Scovillain ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=37,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=951,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pokémon is in play, it is Grass and Fire type.",
            passive=DoubleTypePassive(),
        ),
        Attack(
            title="Spicy Rage",
            game_text="This attack does 70 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_own, 70, base=10),
        ),
    ],
)
