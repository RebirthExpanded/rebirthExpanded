"""Cutiefly (SM - Lost Thunder 145/214 -- JP SM7b 034/050).

Basic Fairy Pokemon. HP 30, weakness Metal x2, resistance Darkness -20,
retreat 0.

  Sweet Scent  [C]  Heal 30 damage from 1 of your Pokemon.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef


async def sweet_scent(ctx):
    damaged = [p for p in ctx.my_pokemon_in_play()
               if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
    target = await ctx.choose_pokemon(
        damaged or ctx.my_pokemon_in_play(), "Choose a Pokémon to heal 30 damage from")
    if target is not None:
        await ctx.heal(30, target)


card = PokemonCardDef(
    guid="0510999b-a7c0-52c0-a8c3-a0bde393966a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    display_name="Cutiefly",
    searchable_by=["Cutiefly", "Basic"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=742,
    abilities=[
        Attack(
            title="Sweet Scent",
            game_text="Heal 30 damage from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=sweet_scent,
        ),
    ],
)
