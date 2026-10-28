"""Vanilluxe (SV4 45 -- JP SV4M 019; English PAR/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



class FrigidRoomPassive(Passive):
    """The opponent's Pokemon with 40 HP or less remaining can't attack."""

    def blocks_attacking(self, pokemon, carrier, board):
        return (pokemon.owning_player_id != carrier.owning_player_id
                and (pokemon.get_attribute(AttrID.HP, 0) or 0) <= 40)


card = PokemonCardDef(
    guid="60d99cf1-115c-5ef1-82d8-4c823f7de81a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Ability(
            title="Frigid Room",
            game_text="Your opponent's Pokémon that have 40 HP or less remaining can't attack.",
            passive=FrigidRoomPassive(),
        ),
        Attack(
            title="Icicle Missile",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=110,
        ),
    ],
)
