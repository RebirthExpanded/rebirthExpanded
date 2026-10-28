"""Seismitoad (SV3 52 -- JP SV3 025; English OBF/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class QuakingZonePassive(Passive):
    """Active: the opponent's Active Pokemon's attacks cost [C] more."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if (pokemon.owning_player_id != carrier.owning_player_id and pc.is_in_active_spot(carrier)
                and board.active_pokemon(pokemon.owning_player_id) is pokemon):
            cost = dict(cost)
            cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


card = PokemonCardDef(
    guid="c1954140-71b4-57f9-af3e-d401092184f2",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Ability(
            title="Quaking Zone",
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon cost Colorless more.",
            passive=QuakingZonePassive(),
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pokémon's Echoed Voice attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            effect=pc.boost_own_next_turn(100, "Echoed Voice"),
        ),
    ],
)
