"""Shinx (SM - Ultra Prism 45/156 -- JP SM5M 017/066, the art here).

Basic Lightning Pokemon. HP 50, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Ability  Evolutionary Advantage  If you go second, this Pokemon can
                                   evolve during your first turn.
  Static Shock [L] 10

Bronzor SM9's passive, verbatim.
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
    guid="7210621f-1995-5d89-874d-16fac9c609d9",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=403,
    abilities=[
        Ability(title="Evolutionary Advantage",
                game_text="If you go second, this Pokémon can evolve during your first turn.",
                passive=EvolutionaryAdvantagePassive()),
        Attack(title="Static Shock", game_text="",
               cost={PokemonTypes.LIGHTNING: 1}, damage=10),
    ],
)
