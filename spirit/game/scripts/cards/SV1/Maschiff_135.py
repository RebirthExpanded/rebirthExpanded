"""Maschiff (SV1 135 -- JP SV1V 053; English SVI/135). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="460d61cd-06db-5737-b4f0-3fa365d0ee6f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    display_name="Maschiff",
    searchable_by=["Maschiff", "Basic"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=942,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Darkness Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
