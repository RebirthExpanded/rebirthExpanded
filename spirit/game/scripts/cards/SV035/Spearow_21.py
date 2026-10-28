"""Spearow (SV035 21 -- JP SV2a 021; English MEW/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.models.board import board_of


class EvolutionaryAdvantagePassive(Passive):
    """Going second: may evolve during your first turn."""

    def may_evolve_early(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        board = board_of(pokemon)
        ts = getattr(board, "turn_state", None) if board is not None else None
        return ts is not None and ts.turn_number == 2 and ts.active_player_id == pokemon.owning_player_id


card = PokemonCardDef(
    guid="73799feb-9579-5dd8-b7fd-00994daef637",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    display_name="Spearow",
    searchable_by=["Spearow", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=21,
    abilities=[
        Ability(
            title="Evolutionary Advantage",
            game_text="If you go second, this Pokémon can evolve during your first turn.",
            passive=EvolutionaryAdvantagePassive(),
        ),
        Attack(
            title="Speed Dive",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
