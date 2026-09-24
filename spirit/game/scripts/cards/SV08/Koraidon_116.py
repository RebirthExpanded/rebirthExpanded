"""Koraidon (SV - Surging Sparks 116/191 -- JP SV8 069/106, the art here).

Basic Fighting Pokemon (Ancient). HP 130, weakness Grass x2, retreat 2.

  Unrelenting Onslaught  [FC] 30+  If 1 of your OTHER Ancient Pokemon
                                   used an attack during your last turn,
                                   this attack does 150 more damage.
  Hammer In              [FCC] 110

The condition reads the attacks-used ledger of my previous turn: any
Ancient Pokemon of mine other than this one, whatever it attacked with.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.data_utils import Attack, PokemonCardDef, subtypes_for

BONUS = 150


def _other_ancient_attacked_last_turn(ctx) -> bool:
    attacker = ctx.attacker
    board = ctx.board
    for used_id, archetype_id, _title in board.turn_state.attacks_used_last_turn:
        if attacker is not None and used_id == attacker.entity_id:
            continue
        user = board.get_entity(used_id)
        if user is not None and user.owning_player_id != ctx.player_id:
            continue
        if "Ancient" in subtypes_for(archetype_id):
            return True
    return False


card = PokemonCardDef(
    guid="6ff0fad3-81e8-5713-968f-879eb670151b",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=116,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=1007,
    abilities=[
        Attack(
            title="Unrelenting Onslaught",
            game_text="If 1 of your other Ancient Pokémon used an attack during your last turn, this attack does 150 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_other_ancient_attacked_last_turn, BONUS),
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)
