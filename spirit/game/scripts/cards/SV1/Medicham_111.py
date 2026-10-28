"""Medicham (SV1 111 -- JP SV1S 039; English SVI/111). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
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


async def acu_punch_ture(ctx):
    await ctx.deal_damage()
    await _lock_one_defender_attack(ctx)


card = PokemonCardDef(
    guid="624ed12f-8998-534b-b3a2-a55330a08098",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Acu-Punch-Ture",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. During your opponent's next turn, that Pokémon can't use that attack.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=acu_punch_ture,
        ),
        Attack(
            title="Kick Shot",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=90,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
