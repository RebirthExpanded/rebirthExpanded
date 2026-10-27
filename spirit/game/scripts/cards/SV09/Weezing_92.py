"""Weezing (SV09 92 -- JP SV9 057; English JTG/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _used_last_turn(title):
    def cond(ctx) -> bool:
        history = ctx.board.turn_state.attacks_prev_turn_by_player.get(ctx.player_id) or []
        return any(used_id == ctx.attacker.entity_id and t == title for used_id, _arch, t in history)
    return cond


card = PokemonCardDef(
    guid="0d73dbf0-2125-5e26-b098-79b49dc54790",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Pervasive Gas",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Crazy Blast",
            game_text="If this Pokémon used Pervasive Gas during your last turn, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_used_last_turn("Pervasive Gas"), 120),
        ),
    ],
)
