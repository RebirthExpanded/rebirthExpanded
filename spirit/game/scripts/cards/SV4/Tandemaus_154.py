"""Tandemaus (SV4 154 -- JP SV4M 056; English PAR/154). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="c1fa2cec-72ba-5c84-9ef6-3c98da776f7d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    display_name="Tandemaus",
    searchable_by=["Tandemaus", "Basic"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=924,
    abilities=[
        Attack(
            title="Tumble Over",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_hit_then_lock,
        ),
    ],
)
