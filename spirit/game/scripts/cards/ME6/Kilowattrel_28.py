"""Kilowattrel (ME6 28 -- JP M6 028; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.models.board import PokemonEntity


def _evolved_this_turn(ctx) -> bool:
    ts = ctx.session.turn_state
    me = ctx.attacker
    return ts.entered_play_turn.get(me.entity_id) == ts.turn_number and any(isinstance(c, PokemonEntity) for c in me.children)


card = PokemonCardDef(
    guid="0452f19d-fc98-5a89-b01f-4c8d5672810e",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name",
    display_name="Kilowattrel",
    searchable_by=["Kilowattrel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Ambush",
            game_text="If this Pokémon evolved from Wattrel during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_this_turn, 90),
        ),
        Attack(
            title="Speed Wing",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
