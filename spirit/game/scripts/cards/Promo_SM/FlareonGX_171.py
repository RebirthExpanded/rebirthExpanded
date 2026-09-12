"""Flareon-GX (SM Black Star Promo SM171 -- JP SMI 001, the art here).

Stage 1 Fire Pokemon-GX, evolves from Eevee. HP 210, weakness Water x2,
no resistance, retreat 2.

  Heat Stage [R] 30  You may attach up to 3 [R] Energy cards from your
                     hand to your Pokemon in any way you like.
  Bright Flame [RRC] 190  Discard 2 [R] Energy from this Pokemon.
  Power Burner-GX [R] 20x  This attack does 20 damage for each [R] Energy
                           card in your discard pile. (You can't use more
                           than 1 GX attack in a game.)

Heat Stage counts Energy CARDS that provide [R] (a Basic Fire, or a
Special Energy that provides it); each picked card chooses its own
Pokemon. Power Burner-GX counts cards in the discard that provide [R].
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import (count_discard, damage_per,
                                                     self_energy_discard_attack)
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Attack, PokemonCardDef


def _fire_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def heat_stage(ctx):
    await ctx.deal_damage()
    pool = [c for c in ctx.hand() if _fire_energy(c)]
    if not pool or not ctx.my_pokemon_in_play():
        return
    picks = await ctx.choose_cards(
        pool, min(3, len(pool)), minimum=0,
        prompt="Choose up to 3 [R] Energy cards to attach to your Pokémon")
    for energy in picks:
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to")
        if target is None:
            target = ctx.attacker
        await ctx.attach_energy(energy, target)


card = PokemonCardDef(
    guid="8e0eb5a6-3a6e-5eb9-a2e6-55c073214ff4",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonGX.Name",
    display_name="Flareon-GX",
    searchable_by=["Flareon-GX", "Stage 1", "GX", "FlareonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=171,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(title="Heat Stage",
               game_text="You may attach up to 3 [R] Energy cards from your hand to your Pokémon in any way you like.",
               cost={PokemonTypes.FIRE: 1},
               damage=30, effect=heat_stage),
        Attack(title="Bright Flame",
               game_text="Discard 2 [R] Energy from this Pokémon.",
               cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
               damage=190,
               effect=self_energy_discard_attack(2, energy_type=PokemonTypes.FIRE)),
        Attack(title="Power Burner-GX",
               game_text="This attack does 20 damage for each [R] Energy card in your discard pile. (You can't use more than 1 GX attack in a game.)",
               cost={PokemonTypes.FIRE: 1},
               damage=20, damage_operator="x", gx=True,
               effect=damage_per(count_discard("mine", _fire_energy), 20)),
    ],
)
