"""Slurpuff (XY - Phantom Forces 69/119 -- JP XY4 062/088, the art here).

Stage 1 Fairy Pokemon (evolves from Swirlix). HP 90, weakness Metal x2,
resistance Darkness -20, retreat 1.

  Tasting      (Ability)  Once during your turn (before your attack), you
                          may draw a card. If this Pokemon is your Active
                          Pokemon, draw 1 more card.
  Light Pulse  [YCC] 60   Prevent all effects of your opponent's attacks,
                          except damage, done to this Pokemon during your
                          opponent's next turn.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot, protect_next_turn
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


async def tasting(ctx):
    await ctx.draw_cards(2 if is_in_active_spot(ctx.source) else 1)


card = PokemonCardDef(
    guid="65002c4a-fdc9-51e4-9f1c-f865cd3177c3",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name",
    display_name="Slurpuff",
    searchable_by=["Slurpuff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    family_id=684,
    abilities=[
        Ability(
            title="Tasting",
            game_text="Once during your turn (before your attack), you may draw a card. If this Pokémon is your Active Pokémon, draw 1 more card.",
            activation=Activations.ONCE_PER_TURN,
            effect=tasting,
        ),
        Attack(
            title="Light Pulse",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=protect_next_turn(effects_too=True),
        ),
    ],
)
