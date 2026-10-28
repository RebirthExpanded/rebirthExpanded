"""Tinkatink (SV4 83 -- JP SV4M 035; English PAR/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="f9beaf93-dbb7-5bbe-a57b-68a97e324dfa",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    display_name="Tinkatink",
    searchable_by=["Tinkatink", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=957,
    abilities=[
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=_hit_then_lock,
        ),
    ],
)
