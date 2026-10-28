"""Silicobra (SV1 119 -- JP SV1S 046; English SVI/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3150d25e-b14e-5e7a-be53-df23d728271d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    display_name="Silicobra",
    searchable_by=["Silicobra", "Basic"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=843,
    abilities=[
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
