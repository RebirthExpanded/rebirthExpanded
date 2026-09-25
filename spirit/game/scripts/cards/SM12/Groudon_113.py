"""Groudon (SM - Cosmic Eclipse 113/236 -- JP SM11a 031/064).

Basic Fighting Pokemon. HP 130, weakness Grass x2, retreat 3.

  Drought           [C]         Attach up to 2 [F] Energy cards from your
                                hand to 1 of your Pokemon.
  Trembling Ground  [FFC] 130   This Pokemon can't use Trembling Ground
                                during your next turn.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.session.effects import is_energy_of_type
from spirit.game.data_utils import Attack, PokemonCardDef


async def drought(ctx):
    cards = [c for c in ctx.hand() if is_energy_of_type(c, PokemonTypes.FIGHTING)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0, prompt="Choose up to 2 Fighting Energy cards to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to")
    if target is None:
        return
    for energy in picks:
        await ctx.attach_energy(energy, target)


card = PokemonCardDef(
    guid="0d5694a4-a99f-515d-8bd9-5f6685d8c778",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=['Groudon', 'Basic', 'Groudon'],
    subtypes=['Basic'],
    collector_number=113,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(title="Drought", game_text="Attach up to 2 Fighting Energy cards from your hand to 1 of your Pokémon.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=drought),
        Attack(title="Trembling Ground",
               game_text="This Pokémon can't use Trembling Ground during your next turn.",
               cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=130,
               locks_next_turn=True),
    ],
)
