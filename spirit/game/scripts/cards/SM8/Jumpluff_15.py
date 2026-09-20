"""Jumpluff (SM - Lost Thunder 15/214 -- JP SM8 011/095, the art here).

Stage 2 Grass Pokemon (evolves from Skiploom). HP 70, weakness Lightning
x2, resistance Fighting -20, retreat 0.

  Lost March  [G] 20x  This attack does 20 damage for each of your Pokemon,
                       except Prism Star Pokemon, in the Lost Zone.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import lost_march_attack
from spirit.game.data_utils import PokemonCardDef

card = PokemonCardDef(
    guid="7ae8ef6e-f4f3-54fc-b039-71e6fa272294",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name",
    display_name="Jumpluff",
    searchable_by=["Jumpluff", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    family_id=187,
    abilities=[lost_march_attack({PokemonTypes.GRASS: 1})],
)
