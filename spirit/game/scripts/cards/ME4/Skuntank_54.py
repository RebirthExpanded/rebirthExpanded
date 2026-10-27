"""Skuntank (ME4 54 -- JP M4 053; English CRI/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="7afe8b14-13a6-525a-9805-18199875aedf",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skuntank.Name",
    display_name="Skuntank",
    searchable_by=["Skuntank", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name",
    family_id=434,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Smash Turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=su.switch_self_attack(),
        ),
    ],
)
