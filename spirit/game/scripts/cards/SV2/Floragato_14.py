"""Floragato (SV2 14 -- JP SV1a 006; English PAL/14, PAL/197, SVP/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="3b9c3081-630d-5d41-844c-991d91694363",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    display_name="Floragato",
    searchable_by=["Floragato", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    family_id=906,
    abilities=[
        Attack(
            title="Seed Bomb",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Magic Whip",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=su.gust_attack(opponent_chooses=True),
        ),
    ],
)
