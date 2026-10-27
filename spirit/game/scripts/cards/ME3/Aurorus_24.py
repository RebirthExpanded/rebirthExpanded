"""Aurorus (ME3 24 -- JP M3 023; English POR/24, POR/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock_defender(ctx):
    await ctx.deal_damage()
    ac.lock_defender_attacks(ctx)
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.models.board import EnergyEntity


def _has_water(target, carrier) -> bool:
    """Tundra Wall: each of this Aurorus's side's Pokemon with Water Energy."""
    return target.owning_player_id == carrier.owning_player_id and any(
        isinstance(e, EnergyEntity) and is_energy_of_type(e, PokemonTypes.WATER) for e in target.children)


card = PokemonCardDef(
    guid="1ea851e3-9f64-5329-816d-55e1b6b08308",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name",
    display_name="Aurorus",
    searchable_by=["Aurorus", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    family_id=698,
    abilities=[
        Ability(
            title="Tundra Wall",
            game_text="All of your Pokémon that have any Water Energy attached take 50 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance). The effect of Tundra Wall doesn't stack.",
            passive=pc.takes_less_passive(50, protects=_has_water, attacker_pred=None, stack_key="Tundra Wall"),
        ),
        Attack(
            title="Freezing Chill",
            game_text="During your opponent's next turn, the Defending Pokémon can't use attacks.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=_hit_then_lock_defender,
        ),
    ],
)
