from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.models.board import board_of
from spirit.game.session.passives import Passive, carrier_pokemon


class StimulatedEvolutionPassive(Passive):
    """With Karrablast in play, both evolution gates (first turn, just
    played) are lifted -- read live, Luxio's Fighting Roar shape."""

    def may_evolve_early(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        board = board_of(pokemon)
        if board is None:
            return False
        return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Karrablast"
                   for p in board.pokemon_in_play(pokemon.owning_player_id))

card = PokemonCardDef(
    guid="ebb58819-ecdf-573e-99d8-a62428b5ca34",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    display_name="Shelmet",
    searchable_by=["Shelmet", "Basic", "Shelmet"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=616,
    abilities=[
        Ability(
            title="Stimulated Evolution",
            game_text="If you have Karrablast in play, this Pok\u00e9mon can evolve during your first turn or the turn you play it.",
            passive=StimulatedEvolutionPassive(),
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
