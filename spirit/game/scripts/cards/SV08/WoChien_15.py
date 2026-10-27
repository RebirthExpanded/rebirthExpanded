"""Wo-Chien (SV08 15 -- JP SV8 010; English SSP/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def hazardous_greed(ctx):
    if len(ctx.deck()) <= 3:
        await ac.snipe_attack(120, pool="bench", count=2, also_base=True)(ctx)
    else:
        await ctx.deal_damage()


async def entangling_whip(ctx):
    await ctx.deal_damage()
    top = list(ctx.deck_top(3))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="19500e9a-86c5-57b7-b30b-0929fe19b790",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WoChien.Name",
    display_name="Wo-Chien",
    searchable_by=["Wo-Chien", "Basic"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=1001,
    abilities=[
        Attack(
            title="Hazardous Greed",
            game_text="If there are 3 or fewer cards in your deck, this attack also does 120 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=hazardous_greed,
        ),
        Attack(
            title="Entangling Whip",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=entangling_whip,
        ),
    ],
)
