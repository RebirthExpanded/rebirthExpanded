"""Absol (SV4 113 -- JP SV3a 036; English PAR/113). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _tooled(ctx) -> bool:
    return ac.has_tool(ctx.attacker)


async def drawareness(ctx):
    hand = list(ctx.hand())
    if len(hand) > 4 and await ctx.ask_yes_no("Discard cards until you have 4 or fewer?"):
        picks = await ctx.discard_from_hand(len(hand), minimum=len(hand) - 4,
                                            prompt="Discard cards until you have 4 or fewer")
    await ctx.draw_until(5)


card = PokemonCardDef(
    guid="566351ff-c472-522b-ba32-b81019fab5c7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=359,
    abilities=[
        Attack(
            title="Drawareness",
            game_text="You may discard any number of cards from your hand until you have 4 or fewer. Draw cards until you have 5 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=drawareness,
        ),
        Attack(
            title="Enhanced Blade",
            game_text="If this Pokémon has a Pokémon Tool attached, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_tooled, 60),
        ),
    ],
)
