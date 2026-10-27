"""Ethan's Pinsir (SV10 1 -- JP SV9a 001; English DRI/1). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _ethan_lost(ctx) -> bool:
    for ko in ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, []):
        name = getattr(def_for(ko.get("archetype_id") or ""), "display_name", "") or ""
        if name.startswith("Ethan's "):
            return True
    return False


card = PokemonCardDef(
    guid="6b8af182-7625-57f6-bb2d-d12ddb05a648",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansPinsir.Name",
    display_name="Ethan's Pinsir",
    searchable_by=["Ethan's Pinsir", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Rallying Horn",
            game_text="If any of your Ethan's Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_ethan_lost, 100),
        ),
    ],
)
