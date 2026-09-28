"""Horror Psychic Energy (SWSH - Rebel Clash 172/192).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [P] Energy."
  "If the [P] Pokemon this card is attached to is in the Active Spot and is
   damaged by an opponent's attack (even if it is Knocked Out), put 2
   damage counters on the Attacking Pokemon."

Spiky Energy's granted ON_DAMAGED_BY_ATTACK hook, limited to a Psychic
holder.
"""

from spirit.game.data_utils import EnergyCardDef, Ability, Triggers
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import is_pokemon_of_type


async def _horror_psychic_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon) or not is_pokemon_of_type(pokemon, PokemonTypes.PSYCHIC):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False, as_counters=True)


card = EnergyCardDef(
    guid="60a4f8db-ab6d-5882-b6be-bfae777a2b38",
    key="SWSH2",
    name="Horror Psychic Energy",
    display_name="Horror Psychic Energy",
    searchable_by=["Horror Psychic Energy", "Special"],
    subtypes=["Special"],
    collector_number=172,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=True,
    provides=[[PokemonTypes.PSYCHIC]],
    granted_abilities=[
        Ability(
            title="Horror Psychic Energy",
            game_text="If the Psychic Pokémon this card is attached to is in the Active Spot and is damaged by an opponent's attack (even if it is Knocked Out), put 2 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_horror_psychic_trigger,
        ),
    ],
)
