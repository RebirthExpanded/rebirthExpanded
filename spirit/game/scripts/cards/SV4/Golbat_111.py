"""Golbat (SV4 111 -- JP SV4K 045; English PAR/111). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _leech(ctx):
    dealt = await ctx.deal_damage()
    if dealt:
        await ctx.heal(dealt, ctx.attacker)


card = PokemonCardDef(
    guid="b6ee1afd-3771-54a0-8c24-d8845f94c679",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    display_name="Golbat",
    searchable_by=["Golbat", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Leech Life",
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_leech,
        ),
    ],
)
