"""Mantine (ME6 17 -- JP M6 017; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def make_waves(ctx):
    for pid in (ctx.player_id, ctx.opponent_id):
        hand = list(ctx.hand(pid))
        if hand:
            await ctx.shuffle_into_deck(hand, pid)
        else:
            await ctx.shuffle_deck(pid)
    await ctx.draw_cards(4)
    await ctx.draw_cards(4, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="aef2307d-4c11-5514-a0f2-ce2b3b6ce5b6",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=458,
    abilities=[
        Attack(
            title="Make Waves",
            game_text="Each player shuffles their hand into their deck. Then, each player draws 4 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=make_waves,
        ),
        Attack(
            title="Bubble Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=su.heal_attack(30),
        ),
    ],
)
