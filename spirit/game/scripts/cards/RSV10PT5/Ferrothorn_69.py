"""Ferrothorn (RSV10PT5 69 -- JP SV11W 064; English WHT/149, WHT/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def power_whip(ctx):
    n = ac.count_energy("self")(ctx)
    if n:
        await ac.snipe_attack(20 * n, pool="any")(ctx)


card = PokemonCardDef(
    guid="d41e99ba-8d6a-5744-9cc5-65e35098486a",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Attack(
            title="Power Whip",
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon for each Energy attached to this Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 1},
            effect=power_whip,
        ),
        Attack(
            title="Metal Claw",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
