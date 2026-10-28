"""Leftovers (SV035 163 -- JP SV2a 160; English GE/99, MEW/163). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.data_utils import Ability, Triggers
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _leftovers(ctx):
    pokemon = ctx.source
    if pokemon is not None and is_in_active_spot(pokemon):
        await ctx.heal(20, pokemon)


card = PokemonToolCardDef(
    guid="f3ae05b2-fb74-51a0-a797-b3c895914b42",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Leftovers.Name",
    display_name="Leftovers",
    searchable_by=["Leftovers", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=163,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Leftovers",
            game_text="At the end of your turn, if the Pokémon this card is attached to is in the Active Spot, heal 20 damage from it.",
            trigger=Triggers.END_OF_TURN,
            effect=_leftovers,
        ),
    ],
)
