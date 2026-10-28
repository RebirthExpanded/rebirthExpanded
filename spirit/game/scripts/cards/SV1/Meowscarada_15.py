"""Meowscarada (SV1 15 -- JP SVAM 006; English SVI/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def trick_cape(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d) or not ctx.attached_energies(d):
        return
    if await ctx.ask_yes_no("Put an Energy attached to your opponent's Active Pokémon into their hand?"):
        picks = await ctx.choose_cards(list(ctx.attached_energies(d)), 1, minimum=1, prompt="Choose an Energy")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="889a53fb-65da-54d4-b8f3-81f33a21f538",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscarada.Name",
    display_name="Meowscarada",
    searchable_by=["Meowscarada", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Attack(
            title="Trick Cape",
            game_text="You may put an Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=trick_cape,
        ),
        Attack(
            title="Flower Blast",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
