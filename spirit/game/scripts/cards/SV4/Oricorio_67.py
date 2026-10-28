"""Oricorio (SV4 67 -- JP SV4M 025; English PAR/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def pep_up(ctx):
    hand = list(ctx.hand())
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    n = len(ctx.my_bench()) + len(ctx.opponent_bench())
    if n:
        await ctx.draw_cards(n)


card = PokemonCardDef(
    guid="e008bbf1-5b64-5399-ac7d-57e27caabf98",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=741,
    abilities=[
        Attack(
            title="Pep Up",
            game_text="Shuffle your hand into your deck. Then, draw a card for each Benched Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pep_up,
        ),
        Attack(
            title="Volt Wave",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
