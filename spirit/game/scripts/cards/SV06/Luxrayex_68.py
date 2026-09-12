"""Luxray ex (SV - Twilight Masquerade 68/167 -- JP SV6 041/101, the art here).

Stage 2 Lightning Pokemon ex, evolves from Luxio. HP 310, weakness Fighting
x2, no resistance, retreat 1.

  Piercing Gaze [CC] 120  Your opponent reveals their hand. Discard a card
                          you find there.
  Volt Strike [LL] 250  Discard all Energy from this Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.data_utils import Attack, PokemonCardDef


async def piercing_gaze(ctx):
    await ctx.deal_damage()
    hand = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Choose a card from your opponent's hand to discard")
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="14005847-bd32-557c-b648-c468ed574351",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxrayex.Name",
    display_name="Luxray ex",
    searchable_by=["Luxray ex", "Stage 2", "ex", "Luxrayex"],
    subtypes=["Stage 2", "ex"],
    collector_number=68,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(title="Piercing Gaze",
               game_text="Your opponent reveals their hand. Discard a card you find there.",
               cost={PokemonTypes.COLORLESS: 2},
               damage=120, effect=piercing_gaze),
        Attack(title="Volt Strike",
               game_text="Discard all Energy from this Pokémon.",
               cost={PokemonTypes.LIGHTNING: 2},
               damage=250, effect=self_energy_discard_attack(all_energy=True)),
    ],
)
