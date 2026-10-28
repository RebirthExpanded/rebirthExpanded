"""Sylveon (SVPJ 70 -- JP SVP 070; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def healing_light(ctx):
    await ctx.deal_damage()
    for p in ctx.my_pokemon_in_play():
        await ctx.heal(10, p)


card = PokemonCardDef(
    guid="9c8b92e8-2a96-51b9-965e-1a7d89c5fcdd",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="SVPJ",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Healing Light",
            game_text="Heal 10 damage from each of your Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=healing_light,
        ),
    ],
)
