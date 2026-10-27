"""Meowstic (ME4 37 -- JP M4 037; English CRI/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def tricky_steps(ctx):
    await ctx.deal_damage()
    target = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if target is None or not bench or ctx.effects_blocked(target) or not ctx.attached_energies(target):
        return
    if not await ctx.ask_yes_no("Move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon?"):
        return
    picks = await ctx.choose_cards(ctx.attached_energies(target), 1, minimum=1, prompt="Choose an Energy to move")
    if picks:
        dest = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)


card = PokemonCardDef(
    guid="9e32c9df-c65a-5d9c-9387-7d8e388aae2a",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=677,
    abilities=[
        Attack(
            title="Tricky Steps",
            game_text="You may move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=tricky_steps,
        ),
    ],
)
