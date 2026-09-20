"""Natu (SM - Lost Thunder 87/214 -- JP SM8 038/095, the art here).

Basic Psychic Pokemon. HP 40, weakness Psychic x2, no resistance, retreat 1.

  Lost March  [CC] 20x  This attack does 20 damage for each of your Pokemon,
                        except Prism Star Pokemon, in the Lost Zone.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import lost_march_attack
from spirit.game.data_utils import PokemonCardDef

card = PokemonCardDef(
    guid="82008e48-4e55-56f0-87fa-78c8b1c014fa",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    display_name="Natu",
    searchable_by=["Natu", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=177,
    abilities=[lost_march_attack({PokemonTypes.COLORLESS: 2})],
)
