"""Nidorina (ME6A 74 -- JP M6a 074; English 30C/88, MEP/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _any_damaged(board, player_id, pokemon) -> bool:
    return any(_counters(board, p) > 0 for p in board.pokemon_in_play(player_id))


card = PokemonCardDef(
    guid="f7bda48f-6d3d-590d-b4e1-129f3085d431",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    display_name="Nidorina",
    searchable_by=["Nidorina", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranFemale.Name",
    family_id=29,
    abilities=[
        Ability(
            title="Share Happiness",
            game_text="Once during your turn, you may use this Ability. Heal 30 damage from 1 of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_any_damaged,
            effect=su.heal_targets(30, "choice"),
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
