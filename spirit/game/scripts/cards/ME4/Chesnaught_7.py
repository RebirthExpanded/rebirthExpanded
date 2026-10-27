"""Chesnaught (ME4 7 -- JP M4 007; English CRI/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def needly_armor(ctx):
    attacker = ctx.damaged_by
    if attacker is None or ctx.effects_blocked(attacker):
        return
    grass = sum(1 for e in ctx.attached_energies(ctx.source) if is_energy_of_type(e, PokemonTypes.GRASS))
    if grass:
        await ctx.deal_damage(30 * grass, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)


card = PokemonCardDef(
    guid="7c9c6e94-48a3-5f8d-9555-7ca3413a170e",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chesnaught.Name",
    display_name="Chesnaught",
    searchable_by=["Chesnaught", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name",
    family_id=650,
    abilities=[
        Ability(
            title="Needly Armor",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), place 3 damage counters on the Attacking Pokémon for each Grass Energy attached to this Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=lambda c: pc.hit_in_active_by_opponent(c) and not c.effects_blocked(c.damaged_by),
            effect=needly_armor,
        ),
        Attack(
            title="Impound",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
