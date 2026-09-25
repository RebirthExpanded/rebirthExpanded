"""Audino (SM - Unified Minds 177/236 -- JP SM10b 040/054).

Basic Colorless Pokemon. HP 90, weakness Fighting x2, retreat 1.

  Ability  Hearing  Once during your turn (before your attack), if this
                    Pokemon is your Active Pokemon, you may draw a card.
  Drain Slap  [CC] 30  Heal 30 damage from this Pokemon.

Activating the Ability is the "you may"; it is not offered from the Bench.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


async def hearing(ctx):
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="98e95ab3-8c37-556f-954e-7c551eebf134",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=['Audino', 'Basic', 'Audino'],
    subtypes=['Basic'],
    collector_number=177,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Ability(
            title="Hearing",
            game_text="Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=hearing,
        ),
        Attack(title="Drain Slap", game_text="Heal 30 damage from this Pokémon.",
               cost={PokemonTypes.COLORLESS: 2}, damage=30,
               effect=heal_attack(30, target="self")),
    ],
)
