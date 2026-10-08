"""Dragonite (SM - Team Up 119/181 -- JP SM9 065/095, the art here).

Stage 2 Dragon Pokemon, evolves from Dragonair. HP 160, weakness Fairy x2,
retreat 3.

  Ability: Fast Call  Once during your turn (before your attack), you may
                      search your deck for a Supporter card, reveal it, and
                      put it into your hand. Then, shuffle your deck.
  Dragon Claw [WLC] 120
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.session.effects import is_supporter_card


def _fast_call_usable(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def fast_call(ctx):
    picks = await ctx.search_deck(
        is_supporter_card, count=1, minimum=0,
        prompt="Choose a Supporter card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="f7ac2354-65b8-5896-b717-e2e99da6a866",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=119,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Fast Call",
            game_text="Once during your turn (before your attack), you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_fast_call_usable,
            effect=fast_call,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
