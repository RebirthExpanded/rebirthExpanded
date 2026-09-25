"""Dratini (SM - Team Up 117/181 -- JP SM9 061/095).

Basic Dragon Pokemon. HP 70, weakness Fairy x2, retreat 2.

  Ability  Defensive Scales  Prevent all effects of your opponent's attacks,
                             except damage, done to this Pokemon.
  Rain Splash  [W] 10
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


card = PokemonCardDef(
    guid="84326555-6007-53f0-999e-06deb3fc1ff5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=['Dratini', 'Basic', 'Dratini'],
    subtypes=['Basic'],
    collector_number=117,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=147,
    abilities=[
        Ability(
            title="Defensive Scales",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pokémon.",
            passive=attack_effect_shield_passive(),
        ),
        Attack(title="Rain Splash", game_text="",
               cost={PokemonTypes.WATER: 1}, damage=10),
    ],
)
