"""Zebstrika (RSV10PT5 32 -- JP SV11W 029; English WHT/115, WHT/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="32fdcd64-dd6e-5f6f-9b94-b43451e74a55",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Electrobullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
    ],
)
