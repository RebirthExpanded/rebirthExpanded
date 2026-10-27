"""Kyurem ex (ZSV10PT5 28 -- JP SV11B 031; English BLK/157, BLK/165, BLK/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def blizzard_burst(ctx):
    n = ac.count_prizes_taken("opponent")(ctx)
    if n:
        await ac.spread_damage(10 * n, also_base=True)(ctx)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="c4b978a1-1e83-51db-b1be-486e084f4766",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyuremex.Name",
    display_name="Kyurem ex",
    searchable_by=["Kyurem ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=28,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Blizzard Burst",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon for each Prize card your opponent has taken. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=blizzard_burst,
        ),
    ],
)
