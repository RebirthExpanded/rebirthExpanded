"""Dratini (SM - Unified Minds 148/236 -- JP SM11 055/094).

Basic Dragon Pokemon. HP 60, weakness Fairy x2, retreat 2.

  Ability  Aqua Lift  If this Pokemon has any [W] Energy attached to it, it
                      has no Retreat Cost.
  Jump On  [CC] 10+   Flip a coin. If heads, this attack does 30 more damage.

Entei (CZ)'s retreat_free_when shape.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.models.board import BoardState
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


def _has_water_energy(pokemon, carrier) -> bool:
    return pokemon is carrier and any(
        energy_provides_type(e, PokemonTypes.WATER.value)
        for e in BoardState.attached_energies(pokemon))


card = PokemonCardDef(
    guid="2c5e6c17-cc92-5d38-bd37-175d0150285a",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=['Dratini', 'Basic', 'Dratini'],
    subtypes=['Basic'],
    collector_number=148,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=147,
    abilities=[
        Ability(
            title="Aqua Lift",
            game_text="If this Pokémon has any Water Energy attached to it, it has no Retreat Cost.",
            passive=retreat_free_when(_has_water_energy),
        ),
        Attack(title="Jump On", game_text="Flip a coin. If heads, this attack does 30 more damage.",
               cost={PokemonTypes.COLORLESS: 2}, damage=10, damage_operator="+",
               effect=flip_bonus(30)),
    ],
)
