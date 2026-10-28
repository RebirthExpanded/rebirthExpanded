"""Lickitung (SV035 108 -- JP SV2a 108; English MEW/108). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock_defender(ctx):
    await ctx.deal_damage()
    ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="6c90b511-7b95-595f-83f9-4305ef1b2b8e",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=108,
    abilities=[
        Attack(
            title="Tongue-Tied",
            game_text="During your opponent's next turn, the Defending Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=_hit_then_lock_defender,
        ),
    ],
)
