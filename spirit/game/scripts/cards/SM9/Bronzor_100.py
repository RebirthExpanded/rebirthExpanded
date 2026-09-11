"""Bronzor (SM - Team Up 100/181 -- JP SM8b 035/? "Dark Order").

Basic Metal Pokemon. HP 50, weakness Fire x2, resistance Psychic -20,
retreat 1.

  Ability  Evolutionary Advantage  If you go second, this Pokemon can
                                   evolve during your first turn.
  Tackle  [MC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.models.board import board_of
from spirit.game.session.passives import Passive, carrier_pokemon


class EvolutionaryAdvantagePassive(Passive):
    def may_evolve_early(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        board = board_of(pokemon)
        ts = getattr(board, "turn_state", None) if board is not None else None
        return ts is not None and ts.turn_number == 2 \
            and ts.active_player_id == pokemon.owning_player_id


card = PokemonCardDef(
    guid="3e26c5be-15f0-5ca7-b3b3-5d213486f464",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=436,
    abilities=[
        Ability(title="Evolutionary Advantage",
                game_text="If you go second, this Pokémon can evolve during your first turn.",
                passive=EvolutionaryAdvantagePassive()),
        Attack(title="Tackle", game_text="",
               cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=20),
    ],
)
