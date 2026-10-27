"""Lurantis ex (ME5 4 -- JP M5 004; English PBL/4, PBL/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


def _healed_this_turn(ctx) -> bool:
    return ctx.attacker.entity_id in ctx.session.turn_state.healed_entities


card = PokemonCardDef(
    guid="9583cee9-a9d2-5771-a493-0138f08edfda",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lurantisex.Name",
    display_name="Lurantis ex",
    searchable_by=["Lurantis ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=4,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=753,
    abilities=[
        Attack(
            title="Lively Cutter",
            game_text="If this Pokémon was healed during this turn, this attack does 200 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_healed_this_turn, 200),
        ),
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=pc.protect_next_turn(reduce=50),
        ),
    ],
)
