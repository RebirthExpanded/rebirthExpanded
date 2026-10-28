"""Latias (SVP 139 -- JP SVP 119; English SVP/139). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class _TypeFloat(Passive):
    """Energy of the type attached: no Retreat Cost."""

    def __init__(self, ptype):
        self.ptype = ptype

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and any(is_energy_of_type(e, self.ptype) for e in pokemon.children):
            return 0
        return cost


card = PokemonCardDef(
    guid="5d59dd74-2195-5892-b532-b0d8fad9aef0",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic"],
    subtypes=["Basic"],
    collector_number=139,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=380,
    abilities=[
        Ability(
            title="Mist Float",
            game_text="If this Pokémon has any Psychic Energy attached, it has no Retreat Cost.",
            passive=_TypeFloat(PokemonTypes.PSYCHIC),
        ),
        Attack(
            title="Psychic Sphere",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
