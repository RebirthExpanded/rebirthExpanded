"""Metagross (SV05 115 -- JP SV5M 048; English TEF/115, TEF/178). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6faabc70-7641-5cb5-962f-30f824f6c3a1",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=115,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Meteor Mash",
            game_text="During your next turn, this Pokémon's Meteor Mash attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=60,
            effect=pc.boost_own_next_turn(60, "Meteor Mash"),
        ),
        Attack(
            title="Luster Blast",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
