"""Furret (SV09 119 -- JP SV9 077; English JTG/119, JTG/168). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c5e99340-b57d-53e0-9ce5-eb89c43e51b6",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name",
    display_name="Furret",
    searchable_by=["Furret", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    family_id=161,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Jet Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
