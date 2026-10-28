"""Articuno (SV035 144 -- JP SV2a 144; English MEW/144). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class IceFloatPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and any(is_energy_of_type(e, PokemonTypes.WATER) for e in pokemon.children):
            return 0
        return cost


card = PokemonCardDef(
    guid="c54fb8ce-179d-5d38-8d2d-8c8a82f4cd43",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=144,
    abilities=[
        Ability(
            title="Ice Float",
            game_text="If this Pokémon has any Water Energy attached, it has no Retreat Cost.",
            passive=IceFloatPassive(),
        ),
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 3},
            damage=110,
            effect=ac.spread_damage(10, also_base=True),
        ),
    ],
)
