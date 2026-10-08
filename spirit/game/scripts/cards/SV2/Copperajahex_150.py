"""Copperajah ex (SV - Paldea Evolved 150/193 -- JP SV2P 054/071, the art
here).

Stage 1 Metal Pokemon ex, evolves from Cufant. HP 300, weakness Fire x2,
resistance Grass -30, retreat 4.

  Ability: Bronze Body  This Pokemon takes 30 less damage from attacks
                        (after applying Weakness and Resistance).
  Nosequake [MMC] 260  This attack also does 30 damage to each of your
                       Benched Pokemon. (Don't apply Weakness and Resistance
                       for Benched Pokemon.)
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef


async def nosequake(ctx):
    await ctx.deal_damage()
    for pokemon in list(ctx.my_bench()):
        await ctx.deal_damage(30, target=pokemon)


card = PokemonCardDef(
    guid="c3c96bd6-9585-50b5-badb-89facd37e601",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajahex.Name",
    display_name="Copperajah ex",
    searchable_by=["Copperajah ex", "Stage 1", "ex", "Copperajahex"],
    subtypes=["Stage 1", "ex"],
    collector_number=150,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Ability(
            title="Bronze Body",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Nosequake",
            game_text="This attack also does 30 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=nosequake,
        ),
    ],
)
