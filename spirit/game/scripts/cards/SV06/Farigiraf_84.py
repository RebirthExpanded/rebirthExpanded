"""Farigiraf (SV06 84 -- JP SV5a 035; English TWM/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_stage1_pokemon


card = PokemonCardDef(
    guid="7031850c-7d96-5e50-8700-ba7e2c27027b",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farigiraf.Name",
    display_name="Farigiraf",
    searchable_by=["Farigiraf", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    family_id=203,
    abilities=[
        Attack(
            title="One-derful Rumble",
            game_text="This attack does 40 damage for each of your Stage 1 Pokémon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine", is_stage1_pokemon), 40),
        ),
        Attack(
            title="Eerie Wave",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
