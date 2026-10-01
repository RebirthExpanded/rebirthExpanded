"""Dangerous Energy (XY - Ancient Origins 82/98 -- JP XY7 081/081).

Special Energy.

  "This card can only be attached to [D] Pokemon. This card provides [D]
   Energy only while this card is attached to a [D] Pokemon. If the [D]
   Pokemon this card is attached to is your Active Pokemon and is damaged by
   an opponent's Pokemon-EX's attack, put 2 damage counters on the
   Attacking Pokemon. (If this card is attached to anything other than a
   [D] Pokemon, discard this card.)"

Spiky Energy (SV09)'s damaged-by-attack grant, limited to Pokemon-EX
(the uppercase XY/BW mechanic) and on Strong Energy's type-locked shape.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, subtypes_for
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.card_effects.passives_common import hit_in_active_by_opponent


def _darkness_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.DARKNESS)


async def _dangerous_energy_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    if "EX" not in subtypes_for(attacker.archetype_id):
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False, as_counters=True)


card = EnergyCardDef(
    guid="6bb826c4-dc36-55ac-a62b-63008131b833",
    key="XY7",
    name="Dangerous Energy",
    display_name="Dangerous Energy",
    searchable_by=["Dangerous Energy", "Special", "DangerousEnergy"],
    subtypes=["Special"],
    collector_number=82,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    attach_to=_darkness_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.DARKNESS]],
    granted_abilities=[
        Ability(
            title="Dangerous Energy",
            game_text="If the Darkness Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's Pokémon-EX's attack, put 2 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=lambda c: hit_in_active_by_opponent(c) and 'EX' in subtypes_for(c.damaged_by.archetype_id),
            effect=_dangerous_energy_trigger,
        ),
    ],
)
