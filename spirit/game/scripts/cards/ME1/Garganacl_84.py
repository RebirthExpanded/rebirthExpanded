"""Garganacl (ME1 84 -- JP M1L 036; English MEG/147, MEG/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _fighting(pokemon) -> bool:
    return PokemonTypes.FIGHTING.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="9775126e-d6e9-5782-9358-e0f81dabc87e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name",
    display_name="Garganacl",
    searchable_by=["Garganacl", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=84,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=932,
    abilities=[
        Ability(
            title="Powerful a-Salt",
            game_text="Attacks used by your Fighting Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=pc.team_damage_boost_passive(30, attacker_pred=_fighting),
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
