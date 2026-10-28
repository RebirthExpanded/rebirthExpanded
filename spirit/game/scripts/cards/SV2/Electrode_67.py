"""Electrode (SV2 67 -- JP SVC 004; English PAL/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="f5de6587-dfd8-5a22-871f-4d55908ad246",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Lightning Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
