"""Alolan Graveler (SV09 45 -- JP SVM 040; English JTG/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="2ab17fc4-efe9-5465-8ccd-1be7689b1198",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    display_name="Alolan Graveler",
    searchable_by=["Alolan Graveler", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Electric Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
