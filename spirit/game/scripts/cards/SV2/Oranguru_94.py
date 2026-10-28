"""Oranguru (SV2 94 -- JP SV1a 039; English PAL/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def _lock_one_defender_attack(ctx):
    """Choose 1 of the opponent's Active Pokemon's attacks; it can't use it
    during the opponent's next turn (Krokorok's Torment shape)."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [e for e in (defender.get_attribute(AttrID.PIE_ABILITIES) or [])
               if isinstance(e, dict) and e.get("abilityType") == "Attack" and e.get("abilityID")]
    if not entries:
        return
    index = 0
    if len(entries) > 1:
        index = await ctx.choose("Choose an attack to lock",
                                 [e.get("title", {}).get("id", "Attack") for e in entries])
    state = ctx.session.turn_state
    state.attack_locks[(defender.entity_id, entries[index]["abilityID"])] = state.turn_number + 1


async def plotters_command(ctx):
    await ctx.deal_damage()
    await _lock_one_defender_attack(ctx)


card = PokemonCardDef(
    guid="5a2b5430-1a8b-5edf-8a40-fea069d38e18",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=765,
    abilities=[
        Attack(
            title="Plotter's Command",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. During your opponent's next turn, that Pokémon can't use that attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=plotters_command,
        ),
        Attack(
            title="Super Psy Bolt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
