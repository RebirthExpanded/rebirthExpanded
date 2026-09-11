"""Ultra Necrozma (SM - Cosmic Eclipse 164/236 -- JP SM12 072/098).

Basic Dragon Pokemon. HP 110, weakness Fairy x2, retreat 2.

  Ability  Ultra Burst  This Pokemon can't attack unless your opponent has
                        2 or fewer Prize cards remaining.
  Luster of Downfall  [PM] 170  Discard an Energy from your opponent's
                                Active Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.support_common import prizes_remaining
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class UltraBurstPassive(Passive):
    def blocks_attacking(self, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        opponent = next((pid for pid in board.player_ids
                         if pid != pokemon.owning_player_id), None)
        return opponent is None or prizes_remaining(board, opponent) > 2


card = PokemonCardDef(
    guid="52e2c340-9d1f-57cc-b1b7-c46f71502adc",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UltraNecrozma.Name",
    display_name="Ultra Necrozma",
    searchable_by=["Ultra Necrozma", "Basic", "UltraNecrozma"],
    subtypes=["Basic"],
    collector_number=164,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=800,
    abilities=[
        Ability(
            title="Ultra Burst",
            game_text="This Pokémon can't attack unless your opponent has 2 or fewer Prize cards remaining.",
            passive=UltraBurstPassive(),
        ),
        Attack(
            title="Luster of Downfall",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=170,
            effect=discard_opponent_energy_attack(count=1),
        ),
    ],
)
