"""Baxcalibur (SV - Paldea Evolved 60/193 -- JP SV2P 027/071).

Stage 2 Water Pokemon, evolves from Arctibax. HP 160, weakness Metal x2,
retreat 2.

  Ability  Super Cold  As often as you like during your turn, you may
                       attach a Basic [W] Energy card from your hand to 1
                       of your Pokemon.
  Buster Tail  [WWC] 130

One use keeps attaching until the player is done (declining the Energy
picker ends it).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_energy


def _basic_water_energy(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def super_cold(ctx):
    while True:
        pool = [c for c in ctx.hand() if _basic_water_energy(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose a Basic [W] Energy card to attach (or Done)")
        if not picks:
            return
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(),
                                          "Choose a Pokémon to attach the Energy to")
        if target is None:
            return
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="7b57493f-beaa-55a6-ba81-0b7c76877535",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baxcalibur.Name",
    display_name="Baxcalibur",
    searchable_by=["Baxcalibur", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=60,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arctibax.Name",
    family_id=996,
    regulation_mark="G",
    abilities=[
        Ability(title="Super Cold",
                game_text="As often as you like during your turn, you may attach a Basic [W] Energy card from your hand to 1 of your Pokémon.",
                activation=Activations.UNLIMITED,
                condition=requires_hand(_basic_water_energy, 1, exclude_self=False),
                effect=super_cold),
        Attack(title="Buster Tail", game_text="",
               cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=130),
    ],
)
