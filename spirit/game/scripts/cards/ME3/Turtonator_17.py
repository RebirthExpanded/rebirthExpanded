"""Turtonator (ME3 17 -- JP M3 017; English POR/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


async def shell_spikes(ctx):
    attacker = ctx.damaged_by
    if attacker is None or ctx.effects_blocked(attacker) or not ctx.attached_energies(attacker):
        return
    await ctx.discard_energy_from(attacker, 1, minimum=1, prompt="Choose an Energy to discard from the Attacking Pokémon")


card = PokemonCardDef(
    guid="1d766357-42d9-5d21-9db9-bfa01b66b1d7",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Ability(
            title="Shell Spikes",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), discard an Energy from the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=lambda c: pc.hit_in_active_by_opponent(c) and not c.effects_blocked(c.damaged_by),
            effect=shell_spikes,
        ),
        Attack(
            title="Heat Breath",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.flip_bonus(80),
        ),
    ],
)
