"""Exeggutor (ME1 5 -- JP M1L 005; English MEG/135, MEG/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="34df9bfa-a935-5520-8529-2970d94e91b0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=pc.protect_next_turn(reduce=30),
        ),
        Attack(
            title="Stomping Wood",
            game_text="This attack does 30 more damage for each Grass Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.GRASS), 30, base=60),
        ),
    ],
)
