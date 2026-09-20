"""Cottonee (SM - Lost Thunder 143/214 -- JP SM12a 097/173, the art here).

Basic Fairy Pokemon. HP 40, weakness Metal x2, resistance Darkness -20, retreat 1.

  Lost March  [CC] 20x  This attack does 20 damage for each of your Pokemon,
                        except Prism Star Pokemon, in the Lost Zone.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import lost_march_attack
from spirit.game.data_utils import PokemonCardDef

card = PokemonCardDef(
    guid="817a7c23-5146-5b97-b900-2ce0b4250ece",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    display_name="Cottonee",
    searchable_by=["Cottonee", "Basic"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=546,
    abilities=[lost_march_attack({PokemonTypes.COLORLESS: 2})],
)
