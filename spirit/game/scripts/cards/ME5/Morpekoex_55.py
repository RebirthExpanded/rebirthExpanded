"""Morpeko ex (ME5 55 -- JP M5 053; English PBL/102, PBL/117, PBL/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own_counters(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


card = PokemonCardDef(
    guid="1ba69236-ca3c-5f56-a652-bcf5cd4f4d2c",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpekoex.Name",
    display_name="Morpeko ex",
    searchable_by=["Morpeko ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=55,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Wheely Draw",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=su.shuffle_hand_into_deck_draw(6),
        ),
        Attack(
            title="Hangry Blaster",
            game_text="This attack does 40 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            damage_operator="+",
            effect=ac.damage_per(_own_counters, 40, base=40),
        ),
    ],
)
