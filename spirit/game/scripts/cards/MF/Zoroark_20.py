"""Zoroark (MF 20 -- JP MF 020; English 30C/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class NighttimeBywayPassive(Passive):
    """While this Pokemon is on the Bench, your Active Pokemon's Retreat Cost
    is 2 less (an Ability)."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier.owning_player_id != pokemon.owning_player_id or not pc.is_in_active_spot(pokemon):
            return cost
        if carrier._containing_area_name() != "bench":
            return cost
        return max(0, cost - 2)


card = PokemonCardDef(
    guid="f458849b-f66a-5a51-927a-b2b17eca18d4",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Ability(
            title="Nighttime Byway",
            game_text="As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is 2 less.",
            passive=NighttimeBywayPassive(),
        ),
        Attack(
            title="Slashing Claw",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)
