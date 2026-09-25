"""Kyogre (SM - Cosmic Eclipse 53/236 -- JP SM11a 021/064).

Basic Water Pokemon. HP 130, weakness Grass x2, retreat 3.

  High Water      [C]         Attach 2 [W] Energy cards from your discard
                              pile to 1 of your Pokemon.
  Swirling Waves  [WWCC] 130  Discard an Energy from this Pokemon.

Both Energy go onto the same Pokemon; with only one in the discard pile it
attaches that one.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.session.effects import is_energy_of_type
from spirit.game.data_utils import Attack, PokemonCardDef


def _water_energy_card(card) -> bool:
    return is_energy_of_type(card, PokemonTypes.WATER)


card = PokemonCardDef(
    guid="bd9035c6-1680-574e-b004-e5c1ccb99b30",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=['Kyogre', 'Basic', 'Kyogre'],
    subtypes=['Basic'],
    collector_number=53,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Attack(title="High Water", game_text="Attach 2 Water Energy cards from your discard pile to 1 of your Pokémon.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=attach_from_discard(_water_energy_card, count=2, target="choice", prompt="Choose 2 Water Energy cards to attach")),
        Attack(title="Swirling Waves", game_text="Discard an Energy from this Pokémon.",
               cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2}, damage=130,
               effect=self_energy_discard_attack(count=1)),
    ],
)
