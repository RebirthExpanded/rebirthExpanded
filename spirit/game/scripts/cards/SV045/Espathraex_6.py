"""Espathra ex (SV045 6 -- JP SV4a 023; English PAF/214, PAF/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac



class DazzlingGazePassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if (pokemon.owning_player_id != carrier.owning_player_id and pc.is_in_active_spot(carrier)
                and board.active_pokemon(pokemon.owning_player_id) is pokemon):
            cost = dict(cost)
            cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


def _both_energy(ctx) -> int:
    return ac.count_energy("self", cards=True)(ctx) + ac.count_energy("defender", cards=True)(ctx)


card = PokemonCardDef(
    guid="1296f62e-d1b0-58a5-8442-015023bfaa5f",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathraex.Name",
    display_name="Espathra ex",
    searchable_by=["Espathra ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=6,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=955,
    passive=TeraRulePassive(),
    abilities=[
        Ability(
            title="Dazzling Gaze",
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon cost Colorless more.",
            passive=DazzlingGazePassive(),
        ),
        Attack(
            title="Psy Ball",
            game_text="This attack does 30 more damage for each Energy attached to both Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(_both_energy, 30, base=30),
        ),
    ],
)
