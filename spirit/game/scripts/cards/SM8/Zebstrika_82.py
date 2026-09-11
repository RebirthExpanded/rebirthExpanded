"""Zebstrika (SM - Lost Thunder 82/214 -- JP SM7a 030/060).

Stage 1 Lightning Pokemon, evolves from Blitzle. HP 110, weakness
Fighting x2, resistance Metal -20, retreat 1.

  Ability  Sprint  Once during your turn (before your attack), you may
                   discard your hand and draw 4 cards.
  Head Bolt  [LC] 60
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


async def sprint(ctx):
    await ctx.discard_cards(list(ctx.hand()))
    await ctx.draw_cards(4)


card = PokemonCardDef(
    guid="cafcc94f-432f-524e-81af-d46065f978c3",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Ability(title="Sprint",
                game_text="Once during your turn (before your attack), you may discard your hand and draw 4 cards.",
                activation=Activations.ONCE_PER_TURN, condition=requires_deck(1),
                effect=sprint),
        Attack(title="Head Bolt", game_text="",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=60),
    ],
)
