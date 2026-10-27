"""Pangoro (ME2PT5 140 -- JP M2a 113; English ASC/140). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _hurt_pancham(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Pancham" and _counters(ctx.board, p) > 0
               for p in ctx.my_bench())


card = PokemonCardDef(
    guid="b18baf41-7b48-51a4-85a1-0e083c67dd9c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name",
    display_name="Pangoro",
    searchable_by=["Pangoro", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    family_id=674,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Master's Punch",
            game_text="If any of your Benched Pancham have any damage counters on them, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_hurt_pancham, 120),
        ),
    ],
)
