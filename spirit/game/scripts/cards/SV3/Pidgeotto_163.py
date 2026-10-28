"""Pidgeotto (SV3 163 -- JP SV3 088; English OBF/163, OBF/208). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4fd17aa9-dbd7-51f3-bb7b-3dd84181d876",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    display_name="Pidgeotto",
    searchable_by=["Pidgeotto", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=163,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Wing Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
