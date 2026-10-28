"""Doublade (SV4 133 -- JP SV4M 044; English PAR/133). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def swords_dance(ctx):
    await pc.apply_own_next_turn_boost(ctx, 80, "Slicing Blade")


card = PokemonCardDef(
    guid="97a16554-ec45-50f0-9126-b905cf8a20db",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    display_name="Doublade",
    searchable_by=["Doublade", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=133,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Swords Dance",
            game_text="During your next turn, this Pokémon's Slicing Blade attack does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            effect=swords_dance,
        ),
        Attack(
            title="Slicing Blade",
            game_text="",
            cost={PokemonTypes.METAL: 2},
            damage=40,
        ),
    ],
)
