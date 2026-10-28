"""Spiritomb (SV1 129 -- JP SV1V 052; English SVI/129). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def doom_decree(ctx):
    results = await ctx.flip_coins(2, "Doom Decree")
    d = ctx.opponent_active()
    if results and all(results) and d is not None and not ctx.effects_blocked(d):
        await ctx.knock_out(d)


card = PokemonCardDef(
    guid="0b745d6f-a25f-5341-af1f-099e63864f8c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Attack(
            title="Taunt",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=su.gust_attack(),
        ),
        Attack(
            title="Doom Decree",
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pokémon is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=doom_decree,
        ),
    ],
)
