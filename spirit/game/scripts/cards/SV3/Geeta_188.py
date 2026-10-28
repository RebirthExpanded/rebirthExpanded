"""Geeta (SV3 188 -- JP SV3 103; English OBF/188, OBF/218, OBF/226). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card

from spirit.game.session.passives import Passive


class _NoAttackThisTurn(Passive):
    def __init__(self, owner, turn):
        self.owner, self.turn = owner, turn

    def blocks_attacking(self, pokemon, carrier, board):
        ts = getattr(board, "turn_state", None)
        return ts is not None and ts.turn_number == self.turn and pokemon.owning_player_id == self.owner


async def geeta(ctx):
    picks = await ctx.search_deck(is_basic_energy_card, count=2, minimum=0, prompt="Choose up to 2 Basic Energy cards to attach to 1 of your Pokémon.")
    if picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon")
        if target is not None:
            for card in picks:
                await ctx.attach_energy(card, target)
    await ctx.shuffle_deck()
    ctx.add_game_passive(_NoAttackThisTurn(ctx.player_id, ctx.session.turn_state.turn_number))


card = SupporterCardDef(
    guid="2b9fdaa7-a6b5-5471-941d-4bf2d152022b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Geeta.Name",
    display_name="Geeta",
    searchable_by=["Geeta", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    effect=geeta,
)
