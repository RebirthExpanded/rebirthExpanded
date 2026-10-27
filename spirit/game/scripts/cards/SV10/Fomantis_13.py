"""Fomantis (SV10 13 -- JP SV10 005; English DRI/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="657698f9-4585-5cc6-b04e-db7227bf0732",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    display_name="Fomantis",
    searchable_by=["Fomantis", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=753,
    abilities=[
        Attack(
            title="Cut Up",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
