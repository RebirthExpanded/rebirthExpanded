"""Togedemaru ex (ME2PT5 149 -- JP MC 514; English ASC/149). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _rolled_last_turn(ctx) -> bool:
    history = ctx.board.turn_state.attacks_prev_turn_by_player.get(ctx.player_id) or []
    return any(used_id == ctx.attacker.entity_id and title == "Spiky Rolling"
               for used_id, _arch, title in history)


card = PokemonCardDef(
    guid="d64a4610-3466-5c54-a4d3-8bd1273c04a3",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaruex.Name",
    display_name="Togedemaru ex",
    searchable_by=["Togedemaru ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=149,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=777,
    abilities=[
        Attack(
            title="Stun Needle",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Spiky Rolling",
            game_text="If this Pokémon used Spiky Rolling during your last turn, this attack does 80 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_rolled_last_turn, 80),
        ),
    ],
)
