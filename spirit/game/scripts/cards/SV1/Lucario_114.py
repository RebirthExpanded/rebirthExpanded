"""Lucario (SV1 114 -- JP SV1S 041; English PAF/174, SVI/114). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _fighting_lost(ctx) -> bool:
    for ko in ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, []):
        d = def_for(ko.get("archetype_id") or "")
        if PokemonTypes.FIGHTING in (getattr(d, "elements", None) or []):
            return True
    return False


card = PokemonCardDef(
    guid="aa4203a5-6f27-59d0-af3c-b8e26b4616ae",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Avenging Knuckle",
            game_text="If any of your Fighting Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_fighting_lost, 120),
        ),
        Attack(
            title="Accelerating Stab",
            game_text="During your next turn, this Pokémon can't use Accelerating Stab.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
