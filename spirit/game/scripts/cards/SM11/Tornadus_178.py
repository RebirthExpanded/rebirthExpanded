"""Tornadus (SM - Unified Minds 178/236 -- JP SM10a 040/054).

Basic Colorless Pokemon. HP 120, weakness Lightning x2, resistance Fighting
-20, retreat 1.

  Knuckle Punch       [C] 20
  Thunderous Tornado  [CCC] 80  If Thundurus is on your Bench, this attack
                                does 20 damage to each of your opponent's
                                Benched Pokemon.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.data_utils import Attack, PokemonCardDef


async def thunderous_tornado(ctx):
    await ctx.deal_damage()
    if any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Thundurus"
           for p in ctx.my_bench()):
        await _spread(ctx)


_spread = spread_damage(20, side="opponent")


card = PokemonCardDef(
    guid="b971cf31-c676-5e81-9e81-7f45a1d281d0",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=['Tornadus', 'Basic', 'Tornadus'],
    subtypes=['Basic'],
    collector_number=178,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=641,
    abilities=[
        Attack(title="Knuckle Punch", game_text="",
               cost={PokemonTypes.COLORLESS: 1}, damage=20),
        Attack(title="Thunderous Tornado", game_text="If Thundurus is on your Bench, this attack does 20 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
               cost={PokemonTypes.COLORLESS: 3}, damage=80,
               effect=thunderous_tornado),
    ],
)
