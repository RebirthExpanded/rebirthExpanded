"""Emboar (SV - White Flare 13/86 -- JP M2a 026, the art here).

Stage 2 Fire Pokemon, evolves from Pignite. HP 180, weakness Water x2, no
resistance, retreat 4.

  Ability  Inferno Fandango  As often as you like during your turn, you may
                             attach a Basic [R] Energy card from your hand
                             to 1 of your Pokemon.
  Heat Crash [RRRC] 120

Baxcalibur's Super Cold shape: one use keeps attaching until the player
declines the Energy picker.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_energy


def _basic_fire_energy(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def inferno_fandango(ctx):
    while True:
        pool = [c for c in ctx.hand() if _basic_fire_energy(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose a Basic [R] Energy card to attach (or Done)")
        if not picks:
            return
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(),
                                          "Choose a Pokémon to attach the Energy to")
        if target is None:
            return
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="581a047e-8f5d-5ae4-82b7-f16ae26e80ce",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emboar.Name",
    display_name="Emboar",
    searchable_by=["Emboar", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    family_id=498,
    abilities=[
        Ability(title="Inferno Fandango",
                game_text="As often as you like during your turn, you may attach a Basic [R] Energy card from your hand to 1 of your Pokémon.",
                activation=Activations.UNLIMITED,
                condition=requires_hand(_basic_fire_energy, 1, exclude_self=False),
                effect=inferno_fandango),
        Attack(title="Heat Crash", game_text="",
               cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1}, damage=120),
    ],
)
