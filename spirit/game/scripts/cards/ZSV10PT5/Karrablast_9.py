"""Karrablast (ZSV10PT5 9 -- JP SV11B 009; English BLK/9, BLK/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.models.board import board_of


class StimulatedEvolutionPassive(Passive):
    """With Shelmet in play, both evolution gates (first turn, just played)
    are lifted (an Ability)."""

    def may_evolve_early(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        board = board_of(pokemon)
        if board is None:
            return False
        return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Shelmet"
                   for p in board.pokemon_in_play(pokemon.owning_player_id))


card = PokemonCardDef(
    guid="f003e340-d4b9-5538-af36-76b1053af070",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast", "Basic"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Ability(
            title="Stimulated Evolution",
            game_text="If you have Shelmet in play, this Pokémon can evolve during your first turn or the turn you play it.",
            passive=StimulatedEvolutionPassive(),
        ),
        Attack(
            title="Horn Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
