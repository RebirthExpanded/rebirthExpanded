"""Erika's Vileplume ex (ME2PT5 3 -- JP MC 003; English ASC/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="9ef206e0-efb2-5fa3-ab0d-1cdee3b753a5",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasVileplumeex.Name",
    display_name="Erika's Vileplume ex",
    searchable_by=["Erika's Vileplume ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=3,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasGloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Lovely Fragrance",
            game_text="Once during your turn, you may use this Ability. Heal 30 damage from each of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            effect=su.heal_targets(30, "each_own"),
        ),
        Attack(
            title="Bloom Powder",
            game_text="Your opponent's Active Pokémon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=ac.condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
    ],
)
