"""Vileplume (ME2 3 -- JP M2 003; English PFL/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _healed_this_turn(ctx) -> bool:
    return ctx.attacker.entity_id in ctx.session.turn_state.healed_entities


card = PokemonCardDef(
    guid="c6f96e34-e7f3-5d22-a5da-019e003f1cfb",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Pollen Bomb",
            game_text="Your opponent's Active Pokémon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
        Attack(
            title="Lively Flower",
            game_text="If this Pokémon was healed during this turn, this attack does 120 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_healed_this_turn, 120),
        ),
    ],
)
