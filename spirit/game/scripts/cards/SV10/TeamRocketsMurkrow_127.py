"""Team Rocket's Murkrow (SV - Destined Rivals 127/182 -- JP M2a 102, the art here).

Basic Darkness Pokemon. HP 80, weakness Lightning x2, resistance Fighting
-30, retreat 1.

  Deceit [C]  Search your deck for a Supporter card, reveal it, and put
              it into your hand. Then, shuffle your deck.
  Torment [DC] 30  Choose 1 of your opponent's Active Pokemon's attacks.
                   During your opponent's next turn, that Pokemon can't
                   use that attack.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_supporter_card


async def torment(ctx):
    """Ralts SWSH12's Memory Skip with 30 damage."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [e for e in (defender.get_attribute(AttrID.PIE_ABILITIES) or [])
               if isinstance(e, dict) and e.get("abilityType") == "Attack"
               and e.get("abilityID")]
    if not entries:
        return
    titles = [e.get("title", {}).get("id", "Attack") for e in entries]
    idx = await ctx.choose("Choose an attack to lock", titles)
    entry = entries[idx]
    ctx.session.turn_state.attack_locks[(defender.entity_id, entry["abilityID"])] = \
        ctx.session.turn_state.turn_number + 1


card = PokemonCardDef(
    guid="860478a6-5e64-55ef-89f6-bf909d3b1c4e",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMurkrow.Name",
    display_name="Team Rocket's Murkrow",
    searchable_by=["Team Rocket's Murkrow", "Basic", "TeamRocketsMurkrow"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=198,
    abilities=[
        Attack(title="Deceit",
               game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
               cost={PokemonTypes.COLORLESS: 1},
               effect=search_to_hand(is_supporter_card, count=1, minimum=0, reveal=True,
                                     prompt="Choose a Supporter card to put into your hand.")),
        Attack(title="Torment",
               game_text="Choose 1 of your opponent's Active Pokémon's attacks. During your opponent's next turn, that Pokémon can't use that attack.",
               cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
               damage=30, effect=torment),
    ],
)
