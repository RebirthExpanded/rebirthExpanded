"""Cyclizar ex (SVP 18 -- JP SVP 009; English SVP/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="fdaeea99-d1e3-587c-9f3c-f8bb3d528f19",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizarex.Name",
    display_name="Cyclizar ex",
    searchable_by=["Cyclizar ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=18,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=967,
    abilities=[
        Attack(
            title="Power Run",
            game_text="Search your deck for a Basic Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=su.search_attach_energy(is_basic_energy_card, count=1, to_self=True, prompt="Choose a Basic Energy card to attach to this Pokémon."),
        ),
        Attack(
            title="Full Throttle",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=_hit_then_lock,
        ),
    ],
)
