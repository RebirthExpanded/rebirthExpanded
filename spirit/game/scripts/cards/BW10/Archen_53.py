"""Archen (BW - Plasma Blast 53/101 -- JP BW9-B 044/076, the art here).

Restored Fighting Pokemon. HP 70, weakness Grass x2, no resistance,
retreat 1.

  Ability  Prehistoric Call  Once during your turn (before your attack),
                             if this Pokemon is in your discard pile, you
                             may put this Pokemon on the bottom of your
                             deck.
  Wing Attack [CC] 20

A RESTORED Pokemon (BW Plasma Blast): not a Basic -- it can't be played
from the hand, placed at setup or found by "Basic Pokemon" searches (the
stage check does all of that) -- it comes into play only through the
Fossil Items that read "put a <name> from the top of your deck onto your
Bench", and evolves into its Stage 1 normally. Prehistoric Call is a
discard-pile Ability (usable_from="discard"), so Garbotoxin's out-of-play
half switches it off.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef



async def prehistoric_call(ctx):
    if not await ctx.ask_yes_no("Put this Pokémon on the bottom of your deck?"):
        return
    await ctx.put_on_bottom_of_deck(ctx.source)



card = PokemonCardDef(
    guid="b23243b0-2ef8-5a0e-96cb-05faeacd5274",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    display_name="Archen",
    searchable_by=["Archen", "Restored"],
    subtypes=["Restored"],
    collector_number=53,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.RESTORED,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    
    family_id=566,
    abilities=[
        Ability(title="Prehistoric Call",
                game_text="Once during your turn (before your attack), if this Pokémon is in your discard pile, you may put this Pokémon on the bottom of your deck.",
                activation=Activations.ONCE_PER_TURN,
                usable_from="discard",
                effect=prehistoric_call),
        Attack(title="Wing Attack", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
