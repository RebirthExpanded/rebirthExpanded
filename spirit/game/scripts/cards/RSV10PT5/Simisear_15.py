"""Simisear (RSV10PT5 15 -- JP SV11W 015; English WHT/100, WHT/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="df46fe7e-b0a2-51b1-9005-e7b5881349d1",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
