"""Gholdengo ex (SV - Paradox Rift 139/182 -- JP SV3a 050/062).

Stage 1 Metal Pokemon ex, evolves from Gimmighoul. HP 260, weakness Fire
x2, resistance Grass -30, retreat 2.

  Ability  Coin Bonus  Once during your turn, you may draw a card. If this
                       Pokemon is in the Active Spot, draw 1 more card.
  Make It Rain  [M] 50x  Discard any number of Basic Energy cards from
                         your hand. This attack does 50 damage for each
                         card you discarded in this way.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import discard_for_bonus
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_energy


async def coin_bonus(ctx):
    await ctx.draw_cards(2 if is_in_active_spot(ctx.source) else 1)


card = PokemonCardDef(
    guid="2d050409-70ca-50e7-be5b-336db9454e2f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengoex.Name",
    display_name="Gholdengo ex",
    searchable_by=["Gholdengo ex", "Stage 1", "ex", "Gholdengoex"],
    subtypes=["Stage 1", "ex"],
    collector_number=139,
    set_code="SV4",
    rarity=Rarities.RareUltra,
    hp=260,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=999,
    regulation_mark="G",
    abilities=[
        Ability(title="Coin Bonus",
                game_text="Once during your turn, you may draw a card. If this Pokémon is in the Active Spot, draw 1 more card.",
                activation=Activations.ONCE_PER_TURN, condition=requires_deck(1),
                effect=coin_bonus),
        Attack(title="Make It Rain",
               game_text="Discard any number of Basic Energy cards from your hand. This attack does 50 damage for each card you discarded in this way.",
               cost={PokemonTypes.METAL: 1}, damage=50,
               effect=discard_for_bonus(source="hand", predicate=is_basic_energy, max_count=60,
                                        per=50, base=0,
                                        prompt="Choose any number of Basic Energy cards to discard")),
    ],
)
