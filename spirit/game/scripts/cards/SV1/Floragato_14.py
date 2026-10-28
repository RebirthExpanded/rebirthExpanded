"""Floragato (SV1 14 -- JP SVAM 005; English SVI/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="8fbc37c8-947c-5b84-8df1-ba94c13df99e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    display_name="Floragato",
    searchable_by=["Floragato", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    family_id=906,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Leaf Step",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
