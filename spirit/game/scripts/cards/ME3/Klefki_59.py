"""Klefki (ME3 59 -- JP M3 058; English POR/59). Japanese art.
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


async def memory_lock(ctx):
    await ctx.deal_damage()
    await _lock_one_defender_attack(ctx)


card = PokemonCardDef(
    guid="923382ec-02ef-5d49-8ada-2eb143f3be2b",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=707,
    abilities=[
        Attack(
            title="Memory Lock",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. During your opponent's next turn, that Pokémon can't use that attack.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=memory_lock,
        ),
    ],
)
