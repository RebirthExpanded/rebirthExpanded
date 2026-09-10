"""Risky Ruins (Mega Evolution 127/132 -- JP M1L 063/063).

Stadium.

  "Whenever any player puts a Basic non-Darkness Pokemon onto their Bench
   during their turn, place 2 damage counters on that Pokemon."

Already in the pool; what changed is when it fires.

Gapejaw Bog says "from their hand", so it watches the bench PLAY. This one
says only "puts onto their Bench during their turn", which is every route
-- a hand play, a Nest Ball out of the deck, Ordinary Rod's partner back
out of the discard. ON_POKEMON_BENCHED used to fire on the hand play
alone, so the deck routes walked past this Stadium untouched. It now fires
on the effect-driven path too and carries ctx.benched_from_hand to tell
the two apart, which leaves Gapejaw Bog a hand-play watcher.

"During their turn" is the other half: an effect that benches a Pokemon
during the OPPONENT's turn is not covered, so this bites only when the
benching player is the turn player.

And "Basic": an evolution card put onto the Bench by an effect is not a
Basic and takes nothing. A Fossil is -- in hand it is an Item, but the
moment it is on the Bench it is a 60-HP Basic Pokemon and takes its two
counters like any other, which is what is_basic_pokemon_in_play answers.
Darkness Pokemon walk in free, which is the printed exception.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_darkness_pokemon
from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.session.effects import is_basic_pokemon_in_play

COUNTERS = 2


async def risky_ruins_watch(ctx):
    """2 damage counters on a Basic non-Darkness Pokémon just benched."""
    pokemon = ctx.benched_pokemon
    if pokemon is None or not is_basic_pokemon_in_play(pokemon):
        return
    if is_darkness_pokemon(pokemon):
        return
    if ctx.benching_player_id != ctx.session.turn_state.active_player_id:
        return
    await ctx.deal_damage(COUNTERS * 10, target=pokemon,
                          apply_modifiers=False, as_counters=True)


card = StadiumCardDef(
    guid="34f2d480-4d64-528e-a379-c5728742136c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RiskyRuins.Name",
    display_name="Risky Ruins",
    searchable_by=["Risky Ruins", "Stadium", "RiskyRuins"],
    subtypes=["Stadium"],
    collector_number=127,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Risky Ruins",
            game_text="Whenever any player puts a Basic non-Darkness Pokémon onto their Bench during their turn, place 2 damage counters on that Pokémon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=risky_ruins_watch,
        ),
    ],
)
