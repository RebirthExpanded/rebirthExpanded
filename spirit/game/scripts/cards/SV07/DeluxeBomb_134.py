"""Deluxe Bomb (SV07 134 -- JP SV7 096; English SCR/134). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.card_effects import passives_common as pc

from spirit.game.data_utils import Ability, Triggers, def_for


async def _deluxe_bomb(ctx):
    pokemon = ctx.source
    attacker = ctx.damaged_by
    if attacker is None or not pc.is_in_active_spot(pokemon) or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(120, target=attacker, apply_modifiers=False, as_counters=True)
    bombs = [c for c in pokemon.children if getattr(def_for(c.archetype_id), "display_name", "") == "Deluxe Bomb"]
    if bombs:
        await ctx.discard_cards(bombs[:1])


card = PokemonToolCardDef(
    guid="6f1ce6e1-ed2a-5bbc-8512-e583429ad317",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DeluxeBomb.Name",
    display_name="Deluxe Bomb",
    searchable_by=["Deluxe Bomb", "Pokémon Tool", "ACE SPEC"],
    subtypes=["Pokémon Tool", "ACE SPEC"],
    collector_number=134,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    granted_abilities=[
        Ability(
            title="Deluxe Bomb",
            game_text="If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 12 damage counters on the Attacking Pokémon. If you placed any damage counters in this way, discard this card.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_deluxe_bomb,
        ),
    ],
)
