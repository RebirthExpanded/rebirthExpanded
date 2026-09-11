"""Slugma (XY - Primal Clash 22/160 -- JP XY5-Bg 011/070).

Basic Fire Pokemon. HP 70, weakness Water x2, retreat 3.

  Grass Fire  [R]      Discard a [G] Energy attached to your opponent's
                       Active Pokemon.
  Ram         [RCC] 30
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_energy_of_type


async def grass_fire(ctx):
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        predicate=lambda c: is_energy_of_type(c, PokemonTypes.GRASS),
        prompt="Choose a Grass Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="f2476b3b-e51b-5c61-9d05-b50a8f615ad9",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Grass Fire",
            game_text="Discard a Grass Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            effect=grass_fire,
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
