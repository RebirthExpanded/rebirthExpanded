"""Wartortle (BWPJ 166 -- JP BWP 166; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="e945b808-25ab-5475-b914-36caf6e57431",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    display_name="Wartortle",
    searchable_by=["Wartortle", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=166,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Smash Turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=su.switch_self_attack(),
        ),
    ],
)
