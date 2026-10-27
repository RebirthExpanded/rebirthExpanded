"""Sandslash (ME6 36 -- JP M6 036; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


async def counter_spikes(ctx):
    attacker = ctx.damaged_by
    if attacker is not None and not ctx.effects_blocked(attacker):
        await ctx.deal_damage(30, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)


card = PokemonCardDef(
    guid="be140f4a-1db3-582d-b4a1-2d3e33426de3",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash",
    searchable_by=["Sandslash", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Ability(
            title="Counter Spikes",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon, put 3 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=lambda c: pc.hit_in_active_by_opponent(c) and not c.effects_blocked(c.damaged_by),
            effect=counter_spikes,
        ),
        Attack(
            title="Digging Claws",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=ac.mill_attack(1),
        ),
    ],
)
