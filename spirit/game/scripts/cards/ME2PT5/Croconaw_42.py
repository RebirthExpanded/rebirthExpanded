"""Croconaw (ME2PT5 42 -- JP MC 167; English ASC/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def crunch(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Crunch")
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target) \
            and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")


card = PokemonCardDef(
    guid="7cab6e1c-d787-5ad3-8788-ca7fbe9d26dd",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    display_name="Croconaw",
    searchable_by=["Croconaw", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            effect=crunch,
        ),
    ],
)
