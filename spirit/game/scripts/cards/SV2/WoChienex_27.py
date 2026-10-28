"""Wo-Chien ex (SV2 27 -- JP SV2P 015; English PAF/240, PAL/232, PAL/257, PAL/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def covetous_ivy(ctx):
    n = ac.count_prizes_taken("opponent")(ctx)
    if n:
        await ac.snipe_attack(60 * n, pool="bench")(ctx)


card = PokemonCardDef(
    guid="abadf61d-266c-54e7-83d1-d569a9ec500e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WoChienex.Name",
    display_name="Wo-Chien ex",
    searchable_by=["Wo-Chien ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=27,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    family_id=1001,
    abilities=[
        Attack(
            title="Covetous Ivy",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pokémon for each Prize card your opponent has taken. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=covetous_ivy,
        ),
        Attack(
            title="Forest Blast",
            game_text="",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
        ),
    ],
)
