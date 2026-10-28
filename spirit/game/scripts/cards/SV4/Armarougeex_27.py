"""Armarouge ex (SV4 27 -- JP SV4K 015; English PAR/218, PAR/27, SVP/125). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10

from spirit.game.attributes import PokemonTypes as _PT


class CrimsonArmorPassive(Passive):
    """Full HP: takes 80 less from opposing attacks (after W/R)."""

    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if calc.is_attack and calc.is_opposing and calc.target is me and _counters(calc.board, me) == 0:
            calc.amount = max(0, calc.amount - 80)


card = PokemonCardDef(
    guid="8031d409-0d56-5b67-a956-65d9fbe13ffa",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarougeex.Name",
    display_name="Armarouge ex",
    searchable_by=["Armarouge ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=27,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Ability(
            title="Crimson Armor",
            game_text="If this Pokémon has full HP, it takes 80 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).",
            passive=CrimsonArmorPassive(),
        ),
        Attack(
            title="Scorching Bazooka",
            game_text="This attack does 40 more damage for each Fire Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.FIRE), 40, base=40),
        ),
    ],
)
