"""Barbaracle (ME - POR 43 -- JP M3 042, the art here).

Stage 1 Fighting Pokemon, evolves from Binacle. HP 130, weakness Grass x2,
no resistance, retreat 2.

  Ability  Stone Arms  Once during your turn, you may use this Ability.
                       Attach a Basic [F] Energy card from your hand to 1
                       of your [F] Pokemon.
  Hammer In [FFC] 80
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_energy, is_pokemon_of_type


def _basic_fighting_energy(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


def _stone_arms_condition(board, player_id, pokemon) -> bool:
    if not requires_hand(_basic_fighting_energy, 1, exclude_self=False)(board, player_id, pokemon):
        return False
    return any(is_pokemon_of_type(p, PokemonTypes.FIGHTING)
               for p in board.pokemon_in_play(player_id))


async def stone_arms(ctx):
    pool = [c for c in ctx.hand() if _basic_fighting_energy(c)]
    targets = [p for p in ctx.my_pokemon_in_play() if is_pokemon_of_type(p, PokemonTypes.FIGHTING)]
    if not pool or not targets:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1,
                                   prompt="Choose a Basic [F] Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your [F] Pokémon to attach the Energy to")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="b5779e15-5c69-5975-a1cc-4326b505407a",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name",
    display_name="Barbaracle",
    searchable_by=["Barbaracle", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    family_id=688,
    abilities=[
        Ability(title="Stone Arms",
                game_text="Once during your turn, you may use this Ability. Attach a Basic [F] Energy card from your hand to 1 of your [F] Pokémon.",
                activation=Activations.ONCE_PER_TURN,
                condition=_stone_arms_condition,
                effect=stone_arms),
        Attack(title="Hammer In", game_text="",
               cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=80),
    ],
)
