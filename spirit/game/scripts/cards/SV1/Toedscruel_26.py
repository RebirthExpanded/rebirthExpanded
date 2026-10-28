"""Toedscruel (SV1 26 -- JP SV1V 011; English SVI/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def eerie_tentacles(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d) or not bench or not ctx.attached_energies(d):
        return
    if not await ctx.ask_yes_no("Move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon?"):
        return
    picks = await ctx.choose_cards(list(ctx.attached_energies(d)), 1, minimum=1, prompt="Choose an Energy to move")
    dest = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon") if picks else None
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


card = PokemonCardDef(
    guid="1cea29e1-056f-5d3d-affe-db2160d34093",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruel.Name",
    display_name="Toedscruel",
    searchable_by=["Toedscruel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    family_id=948,
    abilities=[
        Attack(
            title="Eerie Tentacles",
            game_text="You may move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=eerie_tentacles,
        ),
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=80),
        ),
    ],
)
