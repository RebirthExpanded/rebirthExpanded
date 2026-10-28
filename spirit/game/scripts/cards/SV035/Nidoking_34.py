"""Nidoking (SV035 34 -- JP SV2a 034; English MEW/174, MEW/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



class EnthusiasticKingPassive(Passive):
    """Nidoqueen in play: this Pokemon's attacks cost no Energy."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Nidoqueen"
                                      for p in board.pokemon_in_play(pokemon.owning_player_id)):
            return {}
        return cost


card = PokemonCardDef(
    guid="0bb50f56-cf5e-50e1-92c0-d81bdbd9ad56",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Enthusiastic King",
            game_text="If you have Nidoqueen in play, ignore all Energy in the costs of attacks used by this Pokémon.",
            passive=EnthusiasticKingPassive(),
        ),
        Attack(
            title="Venomous Impact",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=190,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
