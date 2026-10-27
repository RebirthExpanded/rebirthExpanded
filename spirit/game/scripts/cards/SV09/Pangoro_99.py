"""Pangoro (SV09 99 -- JP SV9 062; English JTG/99). Japanese art.
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
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


async def torment(ctx):
    await ctx.deal_damage()
    await _lock_one_defender_attack(ctx)


card = PokemonCardDef(
    guid="82ffc4ad-d712-55f3-a72e-be6ca2e4ee08",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name",
    display_name="Pangoro",
    searchable_by=["Pangoro", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    family_id=674,
    abilities=[
        Attack(
            title="Torment",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. During your opponent's next turn, that Pokémon can't use that attack.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=torment,
        ),
        Attack(
            title="Power Tackle",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_hit_then_lock,
        ),
    ],
)
