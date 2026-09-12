"""Raging Bolt (SV - Stellar Crown 111/142 -- JP SV7 075/102, the art here).

Basic Dragon Pokemon (Ancient). HP 130, no weakness, no resistance,
retreat 3.

  Thunderburst Storm [LF]  This attack does 30 damage to 1 of your
                           opponent's Pokemon for each Energy attached to
                           this Pokemon. (Don't apply Weakness and
                           Resistance for Benched Pokemon.)
  Dragon Headbutt [LFC] 130

Energy is counted as provided (a Double Turbo is 2); W/R apply only when
the chosen target is their Active.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.data_utils import Attack, PokemonCardDef


async def thunderburst_storm(ctx):
    amount = 30 * count_energy("self")(ctx)
    targets = ctx.opponent_pokemon_in_play()
    if amount <= 0 or not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.deal_damage(amount, target=target)


card = PokemonCardDef(
    guid="f881171d-6b56-5cec-8d99-2c4a6e432368",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RagingBolt.Name",
    display_name="Raging Bolt",
    searchable_by=["Raging Bolt", "Basic", "Ancient", "RagingBolt"],
    subtypes=["Basic", "Ancient"],
    collector_number=111,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=1021,
    abilities=[
        Attack(title="Thunderburst Storm",
               game_text="This attack does 30 damage to 1 of your opponent's Pokémon for each Energy attached to this Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
               effect=thunderburst_storm),
        Attack(title="Dragon Headbutt", game_text="",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
               damage=130),
    ],
)
