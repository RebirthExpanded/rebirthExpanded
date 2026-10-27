"""Lokix (SV07 16 -- JP SVI 004; English SCR/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="1879de65-380d-53ab-b941-b1dd4616cea9",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lokix.Name",
    display_name="Lokix",
    searchable_by=["Lokix", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    family_id=919,
    abilities=[
        Attack(
            title="Spiral Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
