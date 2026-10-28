"""Thievul (SV4 120 -- JP SV3a 041; English PAR/120). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_card


async def rob_n_run(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not ctx.hand(ctx.opponent_id) or not await ctx.ask_yes_no("Use Rob-'n'-Run?"):
        return
    hand = list(ctx.hand(ctx.opponent_id))
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    pool = [c for c in hand if is_energy_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=min(2, len(pool)), prompt="Choose 2 Energy cards")
        if picks:
            await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = PokemonCardDef(
    guid="471a9253-dedd-551a-adf9-9f1c3bb00363",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name",
    display_name="Thievul",
    searchable_by=["Thievul", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=120,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    family_id=827,
    abilities=[
        Ability(
            title="Rob-'n'-Run",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may have your opponent reveal their hand, and then you choose 2 Energy cards you find there and shuffle them into your opponent's deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=rob_n_run,
        ),
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
