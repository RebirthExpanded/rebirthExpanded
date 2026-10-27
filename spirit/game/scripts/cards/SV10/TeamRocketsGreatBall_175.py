"""Team Rocket's Great Ball (SV10 175 -- JP SV10 088; English ASC/205, DRI/175). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.data_utils import def_for, subtypes_for


def _named(prefix):
    def pred(card) -> bool:
        return card is not None and (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith(prefix)
    return pred


def _name_has(*parts):
    def pred(card) -> bool:
        name = (getattr(def_for(card.archetype_id), "display_name", "") or "") if card is not None else ""
        return any(p in name for p in parts)
    return pred

from spirit.game.session.effects import is_basic_pokemon, is_evolution_pokemon


def _rocket(card) -> bool:
    return _named("Team Rocket's ")(card)


async def team_rockets_great_ball(ctx):
    results = await ctx.flip_coins(1, "Team Rocket's Great Ball")
    if results and results[0]:
        pred = lambda c: is_evolution_pokemon(c) and _rocket(c)
        prompt = "Choose an Evolution Team Rocket's Pokémon."
    else:
        pred = lambda c: is_basic_pokemon(c) and _rocket(c)
        prompt = "Choose a Basic Team Rocket's Pokémon."
    picks = await ctx.search_deck(pred, count=1, minimum=0, prompt=prompt)
    if picks:
        await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="0aee5cd1-9ed2-5091-8958-0ccfce5022a9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGreatBall.Name",
    display_name="Team Rocket's Great Ball",
    searchable_by=["Team Rocket's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=team_rockets_great_ball,
)
