"""Marowak (SV07 73 -- JP SV7 049; English SCR/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _hurt_cubone(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Cubone" and _counters(ctx.board, p) > 0
               for p in ctx.my_bench())


card = PokemonCardDef(
    guid="5aeeaa86-9d3f-521d-873c-e90701b03b26",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 40 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            effect=pc.debuff_defender_attacks(40),
        ),
        Attack(
            title="Bone Vengeance",
            game_text="If any of your Benched Cubone have any damage counters on them, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_hurt_cubone, 120),
        ),
    ],
)
