"""Pincurchin (SV2 73 -- JP SV2D 022; English PAL/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _stunned_last_turn(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    history = ts.attacks_prev_turn_by_player.get(player_id) or [] if ts is not None else []
    return pokemon is not None and any(used_id == pokemon.entity_id and t == "Stun Needle" for used_id, _a, t in history)


card = PokemonCardDef(
    guid="e659c4a3-f482-5ce7-8045-10346e08c7c7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pincurchin.Name",
    display_name="Pincurchin",
    searchable_by=["Pincurchin", "Basic"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=871,
    abilities=[
        Attack(
            title="Stun Needle",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Follow-Up Kerzap",
            game_text="You can use this attack only if this Pokémon used Stun Needle during your last turn.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=100,
            condition=_stunned_last_turn,
        ),
    ],
)
