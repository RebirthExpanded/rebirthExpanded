"""Masquerain (SV4 2 -- JP SV4M 002; English PAR/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def daunting_eyes(ctx):
    heads = await ctx.flip_until_tails("Daunting Eyes")
    d = ctx.opponent_active()
    if not heads or d is None or ctx.effects_blocked(d):
        return
    pool = list(ctx.attached_energies(d))
    n = min(heads, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt=f"Choose {n} Energy to shuffle into your opponent's deck")
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = PokemonCardDef(
    guid="24dbe94a-a2d5-553b-9a83-4a0673b2c9cf",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Daunting Eyes",
            game_text="Flip a coin until you get tails. For each heads, shuffle an Energy attached to your opponent's Active Pokémon into their deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=daunting_eyes,
        ),
        Attack(
            title="Cutting Wind",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
