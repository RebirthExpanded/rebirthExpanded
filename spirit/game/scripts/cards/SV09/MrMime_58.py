"""Mr. Mime (SV09 58 -- JP SV9 034; English JTG/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def mimic(ctx):
    hand = list(ctx.hand())
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    n = len(ctx.hand(ctx.opponent_id))
    if n:
        await ctx.draw_cards(n)


card = PokemonCardDef(
    guid="2875f87c-3f34-5724-be2c-efc3167a0f0b",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=439,
    abilities=[
        Attack(
            title="Mimic",
            game_text="Shuffle your hand into your deck. Then, draw a card for each card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=mimic,
        ),
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
