"""Slowking (SV085 19 -- JP SVM 028; English PRE/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def wash_the_slate_clean(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d):
        return
    pool = list(ctx.attached_energies(d))
    if pool and await ctx.ask_yes_no("Put 2 Energy attached to your opponent's Active Pokémon into their hand?"):
        n = min(2, len(pool))
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="0fe2d1f8-0f21-54a3-9f17-8a0add760534",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Wash the Slate Clean",
            game_text="You may put 2 Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=wash_the_slate_clean,
        ),
    ],
)
