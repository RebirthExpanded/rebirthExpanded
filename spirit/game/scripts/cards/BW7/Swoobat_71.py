"""Swoobat (BW - Boundaries Crossed 71/149 -- JP BW6-Bc 030/059).

Stage 1 Psychic Pokemon, evolves from Woobat. HP 80, weakness Lightning
x2, resistance Fighting -20, retreat 1.

  Jet Woofer  [P]  For each [P] Energy attached to this Pokemon, discard
                   the top card of your opponent's deck.
  Acrobatics  [CC] 20+  Flip 2 coins. This attack does 20 more damage for
                        each heads.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.data_utils import Attack, PokemonCardDef


async def jet_woofer(ctx):
    n = count_energy("self", PokemonTypes.PSYCHIC)(ctx)
    if n > 0:
        await ctx.discard_cards(ctx.deck_top(n, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="3b9108ce-9bb8-588b-b9e2-e2b03a97528d",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(title="Jet Woofer",
               game_text="For each [P] Energy attached to this Pokémon, discard the top card of your opponent's deck.",
               cost={PokemonTypes.PSYCHIC: 1}, damage=0, effect=jet_woofer),
        Attack(title="Acrobatics", game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
               cost={PokemonTypes.COLORLESS: 2}, damage=20,
               effect=flip_damage(coins=2, bonus_per_heads=20)),
    ],
)
