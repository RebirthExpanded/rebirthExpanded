"""Ariados (SV06 5 -- JP SV5a 005; English TWM/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.session.passives import effective_retreat_cost


class BigNetPassive(Passive):
    """The opponent's Active Evolution Pokemon's Retreat Cost is [C] more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if (pokemon.owning_player_id != carrier.owning_player_id and pc.is_in_active_spot(pokemon)
                and is_evolution_pokemon(pokemon)):
            return cost + 1
        return cost


def _defender_retreat(ctx) -> int:
    d = ctx.opponent_active()
    return effective_retreat_cost(ctx.board, d) if d is not None else 0


card = PokemonCardDef(
    guid="e3207139-f4f4-5106-b7eb-283d737d7831",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Ability(
            title="Big Net",
            game_text="Your opponent's Active Evolution Pokémon's Retreat Cost is Colorless more.",
            passive=BigNetPassive(),
        ),
        Attack(
            title="String Bind",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_defender_retreat, 30, base=10),
        ),
    ],
)
