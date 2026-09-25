"""Charmander (SM - Team Up 12/181 -- JP SM9 011/095).

Basic Fire Pokemon. HP 70, weakness Water x2, retreat 1.

  Ember  [R] 30  Discard an Energy from this Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="00679110-ab31-5cfd-a0d7-47ffc8d5a695",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(title="Ember",
               game_text="Discard an Energy from this Pokémon.",
               cost={PokemonTypes.FIRE: 1}, damage=30,
               effect=self_energy_discard_attack(count=1)),
    ],
)
