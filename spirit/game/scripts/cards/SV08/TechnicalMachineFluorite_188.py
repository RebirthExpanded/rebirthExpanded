"""Technical Machine: Fluorite (SV08 188 -- JP SV8 101; English SSP/188). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10

from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import Ability, Attack, Triggers
from spirit.game.card_effects.trainers import discard_self_tool_at_end_of_turn

TM_FLUORITE = "Technical Machine: Fluorite"


async def fluorite(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool:
        await ctx.discard_cards(pool)
    for p in ctx.my_pokemon_in_play():
        if _has_sub(p, "Tera") and _counters(ctx.board, p) > 0:
            await ctx.heal(_counters(ctx.board, p) * 10, p)


card = PokemonToolCardDef(
    guid="faf643cc-d6ac-5426-bf6f-c161623b5099",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineFluorite.Name",
    display_name="Technical Machine: Fluorite",
    searchable_by=["Technical Machine: Fluorite", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=188,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Fluorite",
            game_text="Discard all Energy from this Pokémon, and heal all damage from each of your Tera Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            effect=fluorite,
        ),
        Ability(
            title=TM_FLUORITE,
            game_text="If this card is attached to 1 of your Pokémon, discard it at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_tool_at_end_of_turn(TM_FLUORITE),
        ),
    ],
)
