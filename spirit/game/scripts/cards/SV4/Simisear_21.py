"""Simisear (SV4 21 -- JP SV4M 011; English PAR/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



class MonkeyTrioPassive(Passive):
    """Simisage, Simisear and Simipour in play: no [C] in attack costs."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier or not cost.get("Colorless"):
            return cost
        names = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in board.pokemon_in_play(pokemon.owning_player_id)}
        if {"Simisage", "Simisear", "Simipour"} <= names:
            cost = dict(cost)
            del cost["Colorless"]
        return cost
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b6780d39-3f4c-536a-9a9d-d6cebcae3567",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Ability(
            title="Monkey Trio",
            game_text="If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.",
            passive=MonkeyTrioPassive(),
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=190,
            effect=ac.recoil_attack(30),
        ),
    ],
)
