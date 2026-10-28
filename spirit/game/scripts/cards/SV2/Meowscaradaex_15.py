"""Meowscarada ex (SV2 15 -- JP SV1a 007; English PAL/15, PAL/231, PAL/256, PAL/271, SVP/33, SVP/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)



def _bouquet_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(other, "bench") if other else None
    return bool(hand) and any(_basic_grass(c) for c in hand.children) and bool(bench and bench.children)


async def bouquet_magic(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=_basic_grass, prompt="Discard a Basic Grass Energy card to use Bouquet Magic.")
    bench = ctx.opponent_bench()
    if not paid or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon to put 3 damage counters on")
    if target is not None:
        await ctx.deal_damage(30, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="aba478dd-c0f9-5e18-a65c-09ae5fff0d8a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscaradaex.Name",
    display_name="Meowscarada ex",
    searchable_by=["Meowscarada ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=15,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Ability(
            title="Bouquet Magic",
            game_text="You must discard a Basic Grass Energy card from your hand in order to use this Ability. Once during your turn, you may put 3 damage counters on 1 of your opponent's Benched Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_bouquet_condition,
            effect=bouquet_magic,
        ),
        Attack(
            title="Scratching Nails",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 120),
        ),
    ],
)
