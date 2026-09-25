"""Golduck (SM - Cosmic Eclipse 41/236 -- JP SM11a 018/064).

Stage 1 Water Pokemon, evolves from Psyduck. HP 110, weakness Grass x2,
retreat 1.

  Scratch      [C] 30
  Energy Loop  [WC] 80  Put an Energy attached to this Pokemon into your hand.

Chien-Pao (SV08)'s shape: damage first, then the Energy goes to hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

from spirit.game.data_utils import Attack, PokemonCardDef


async def energy_loop(ctx):
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.source)
    if not energies:
        return
    picks = energies if len(energies) == 1 else await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose an Energy card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="07565b6a-052d-5c90-a560-cbbea33e232a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=['Golduck', 'Stage 1', 'Golduck'],
    subtypes=['Stage 1'],
    collector_number=41,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(title="Scratch", game_text="",
               cost={PokemonTypes.COLORLESS: 1}, damage=30),
        Attack(title="Energy Loop", game_text="Put an Energy attached to this Pokémon into your hand.",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=80,
               effect=energy_loop),
    ],
)
