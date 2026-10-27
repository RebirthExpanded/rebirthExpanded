"""Smoliv (SV10 21 -- JP MC 069; English DRI/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="03d1dd7b-9bc7-59cd-971d-b33834740623",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    display_name="Smoliv",
    searchable_by=["Smoliv", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=928,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
