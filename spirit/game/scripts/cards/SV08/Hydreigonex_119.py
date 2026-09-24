"""Hydreigon ex (SV - Surging Sparks 119/191 -- JP SV8 072/106, the art here).

Stage 2 Darkness Pokemon-ex (Tera, evolves from Zweilous). HP 330,
weakness Grass x2, retreat 3.

  Tera rule            As long as this Pokemon is on your Bench, prevent
                       all damage done to it by attacks (both yours and
                       your opponent's).
  Crashing Headbutt  [DC] 200    Discard the top 3 cards of your
                                 opponent's deck.
  Obsidian           [DDMC] 130  This attack also does 130 damage to 2 of
                                 your opponent's Benched Pokemon. (Don't
                                 apply Weakness and Resistance for Benched
                                 Pokemon.)
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.data_utils import Attack, PokemonCardDef

MILL = 3
BENCH_HIT = 130


async def crashing_headbutt(ctx):
    await ctx.deal_damage()
    await ctx.discard_cards(ctx.deck_top(MILL, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="d70d7d08-7c81-5ccd-babf-c9a9a31a124f",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigonex.Name",
    display_name="Hydreigon ex",
    searchable_by=["Hydreigon ex", "Stage 2", "ex", "Tera", "Hydreigonex"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=119,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Crashing Headbutt",
            game_text="Discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=crashing_headbutt,
        ),
        Attack(
            title="Obsidian",
            game_text="This attack also does 130 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.METAL: 1,
                  PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=snipe_attack(BENCH_HIT, pool="bench", count=2, also_base=True),
        ),
    ],
)
