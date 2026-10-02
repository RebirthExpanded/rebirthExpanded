"""Team Magma's Secret Base (XY - Double Crisis 32/34 -- JP CP1 032/034, the
art here).

Stadium.

  "Whenever any player puts a Basic Pokemon (except for Team Magma
   Pokemon) from his or her hand onto his or her Bench, put 2 damage
   counters on that Pokemon."

Gapejaw Bog's ON_POKEMON_BENCHED watch with the Team Magma exception. It is
ordered with the benched Pokemon's own "when you play this Pokemon"
Ability by that Pokemon's owner: Dedenne-GX's Dedechange first, or the
counters first -- and with Mimikyu's Shadow Box in play, a Pokemon-GX with
those counters has no Abilities left to use (official Q&A).
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gapejaw_bog_applies, gapejaw_bog_watch
from spirit.game.data_utils import Ability, StadiumCardDef, Triggers, def_for


def _team_magma(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Team Magma's")


def _secret_base_applies(ctx) -> bool:
    return gapejaw_bog_applies(ctx) and not _team_magma(ctx.benched_pokemon)


async def secret_base_watch(ctx):
    if _secret_base_applies(ctx):
        await gapejaw_bog_watch(ctx)


card = StadiumCardDef(
    guid="8c9f31e8-0713-5bf7-be21-30f4571539bc",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmasSecretBase.Name",
    display_name="Team Magma's Secret Base",
    searchable_by=["Team Magma's Secret Base", "Stadium"],
    subtypes=["Stadium"],
    collector_number=32,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Team Magma's Secret Base",
            game_text="Whenever any player puts a Basic Pokémon (except for Team Magma Pokémon) from his or her hand onto his or her Bench, put 2 damage counters on that Pokémon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=secret_base_watch,
            trigger_applies=_secret_base_applies,
        ),
    ],
)
