"""Town Store (SV - Obsidian Flames 196/197 -- JP SV3 107/108).

Stadium.  "Once during each player's turn, that player may search their
deck for a Pokemon Tool card, reveal it, and put it into their hand. Then,
that player shuffles their deck."
"""

from spirit.game.attributes import AttrID, Rarities, TrainerType
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import Ability, Activations, StadiumCardDef


def _is_tool_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def town_store(ctx):
    picks = await ctx.search_deck(_is_tool_card, count=1, minimum=0,
                                  prompt="Choose a Pokémon Tool card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = StadiumCardDef(
    guid="1a76a60c-b272-520d-abf5-bb6b842a34a6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownStore.Name",
    display_name="Town Store",
    searchable_by=["Town Store", "Stadium", "TownStore"],
    subtypes=["Stadium"],
    collector_number=196,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    ability=Ability(title="Town Store",
                    game_text="Once during each player's turn, that player may search their deck for a Pokémon Tool card, reveal it, and put it into their hand. Then, that player shuffles their deck.",
                    activation=Activations.ONCE_PER_TURN, condition=requires_deck(1),
                    effect=town_store),
)
