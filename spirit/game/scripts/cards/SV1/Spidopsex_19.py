"""Spidops ex (SV1 19 -- JP SV1V 008; English SVI/19, SVI/223, SVI/243). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class _TrapTerritory(Passive):
    """The opponent's Active Pokemon's Retreat Cost is [C] more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id != carrier.owning_player_id and pc.is_in_active_spot(pokemon):
            return cost + 1
        return cost
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _defender_retreat(ctx) -> int:
    d = ctx.opponent_active()
    return effective_retreat_cost(ctx.board, d) if d is not None else 0


card = PokemonCardDef(
    guid="86ab085f-8194-5c52-98d9-992c40cc6cca",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spidopsex.Name",
    display_name="Spidops ex",
    searchable_by=["Spidops ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=19,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name",
    family_id=917,
    abilities=[
        Ability(
            title="Trap Territory",
            game_text="Your opponent's Active Pokémon's Retreat Cost is Colorless more.",
            passive=_TrapTerritory(),
        ),
        Attack(
            title="Wire Hang",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.damage_per(_defender_retreat, 30, base=90),
        ),
    ],
)
