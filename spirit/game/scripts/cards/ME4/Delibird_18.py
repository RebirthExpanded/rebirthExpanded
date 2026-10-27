"""Delibird (ME4 18 -- JP M4 018; English CRI/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card



async def _attach_up_to_3(ctx, pid):
    hand = [c for c in ctx.hand(pid) if is_basic_energy_card(c)]
    targets = list(ctx.board.pokemon_in_play(pid))
    if not hand or not targets:
        return
    picks = await ctx.choose_cards(hand, min(3, len(hand)), minimum=0, player_id=pid,
                                   prompt="Attach up to 3 Basic Energy cards from your hand to your Pokémon.")
    for energy in picks:
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon to attach the Energy to", player_id=pid)
        if target is not None:
            await ctx.attach_energy(energy, target)


async def pleasing_present(ctx):
    await _attach_up_to_3(ctx, ctx.opponent_id)
    await _attach_up_to_3(ctx, ctx.player_id)


card = PokemonCardDef(
    guid="390f9108-11e0-53e8-be49-29b805e39d20",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Attack(
            title="Pleasing Present",
            game_text="Each player may attach up to 3 Basic Energy cards from their hand to their Pokémon in any way they like. Your opponent does this first.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pleasing_present,
        ),
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
