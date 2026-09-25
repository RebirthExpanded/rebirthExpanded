"""Palpitoad (SM - Cosmic Eclipse 116/236 -- JP SM11b 032/049).

Stage 1 Fighting Pokemon, evolves from Tympole. HP 90, weakness Grass x2,
retreat 2.

  Mini Earthquake  [F] 60  This attack does 10 damage to each of your
                           Benched Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.data_utils import Attack, PokemonCardDef


_self_spread = spread_damage(10, side="mine")


async def mini_earthquake(ctx):
    await ctx.deal_damage()
    await _self_spread(ctx)


card = PokemonCardDef(
    guid="7e2eeff6-8efd-59e7-86bd-6f0410ae7e0e",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    display_name="Palpitoad",
    searchable_by=['Palpitoad', 'Stage 1', 'Palpitoad'],
    subtypes=['Stage 1'],
    collector_number=116,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    family_id=535,
    abilities=[
        Attack(title="Mini Earthquake", game_text="This attack does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
               cost={PokemonTypes.FIGHTING: 1}, damage=60,
               effect=mini_earthquake),
    ],
)
