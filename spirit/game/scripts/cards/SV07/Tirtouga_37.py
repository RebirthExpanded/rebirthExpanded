"""Tirtouga (SV07 37 -- JP SV7 022; English SCR/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="8cce133b-e632-5a62-a57f-74fb95f35e6d",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    display_name="Tirtouga",
    searchable_by=["Tirtouga", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueCoverFossil.Name",
    family_id=564,
    abilities=[
        Attack(
            title="Splashing Turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            effect=su.switch_self_attack(),
        ),
    ],
)
