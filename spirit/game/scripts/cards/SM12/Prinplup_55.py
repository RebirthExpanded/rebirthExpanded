"""Prinplup (SM - Cosmic Eclipse 55/236 -- JP SM11b 010/049).

Stage 1 Water Pokemon, evolves from Piplup. HP 80, weakness Lightning x2,
retreat 2.

  Water Drip   [W] 20
  Direct Dive  [WWW]  Discard all Energy from this Pokemon. This attack does
                      100 damage to 1 of your opponent's Benched Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.data_utils import Attack, PokemonCardDef


_dive = snipe_attack(100, pool="bench")


async def direct_dive(ctx):
    await ctx.discard_energy_from(ctx.attacker, 99, prompt="Discard all Energy from this Pokémon")
    await _dive(ctx)


card = PokemonCardDef(
    guid="1c6812b8-d012-5db7-9db9-e515afa41543",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    display_name="Prinplup",
    searchable_by=['Prinplup', 'Stage 1', 'Prinplup'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    family_id=393,
    abilities=[
        Attack(title="Water Drip", game_text="",
               cost={PokemonTypes.WATER: 1}, damage=20),
        Attack(title="Direct Dive", game_text="Discard all Energy from this Pokémon. This attack does 100 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
               cost={PokemonTypes.WATER: 3}, damage=0,
               effect=direct_dive),
    ],
)
