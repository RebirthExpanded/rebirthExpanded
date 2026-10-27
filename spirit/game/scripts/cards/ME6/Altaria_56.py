"""Altaria (ME6 56 -- JP M6 056; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import PokemonStage


class CottonCarryPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id and \
                pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value:
            return 0
        return cost


card = PokemonCardDef(
    guid="f4c91828-7c47-56e8-a4fa-dd50ce852e6d",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Cotton Carry",
            game_text="As long as this Pokémon is in play, your Basic Pokémon have no Retreat Cost.",
            passive=CottonCarryPassive(),
        ),
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
