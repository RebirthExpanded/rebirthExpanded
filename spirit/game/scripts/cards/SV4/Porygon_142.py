"""Porygon (SV4 142 -- JP SV4M 048; English PAR/142). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def data_displacement(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Data Displacement")
    d = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if not (results and results[0]) or d is None or d in ctx.knockouts or not bench or not ctx.attached_energies(d):
        return
    picks = await ctx.choose_cards(list(ctx.attached_energies(d)), 1, minimum=1, prompt="Choose an Energy to move")
    dest = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon") if picks else None
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


card = PokemonCardDef(
    guid="92563ddf-e329-55ac-8313-68318f5e7c82",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Data Displacement",
            game_text="Flip a coin. If heads, move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=data_displacement,
        ),
    ],
)
