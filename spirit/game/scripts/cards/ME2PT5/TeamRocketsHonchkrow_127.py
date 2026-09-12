"""Team Rocket's Honchkrow (ME - Ascended Heroes 127 -- JP M2a 103, the art here).

Stage 1 Darkness Pokemon, evolves from Team Rocket's Murkrow. HP 130,
weakness Lightning x2, resistance Fighting -30, retreat 1.

  Rocket Feathers [CC] 60x  You may discard any number of Supporter cards
                            that have "Team Rocket" in their name from
                            your hand, and this attack does 60 damage for
                            each card you discarded in this way.
  Hammer In [DCC] 100
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef, def_for
from spirit.game.session.effects import is_supporter_card


def _team_rocket_supporter(card) -> bool:
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return is_supporter_card(card) and "Team Rocket" in name


async def rocket_feathers(ctx):
    pool = [c for c in ctx.hand() if _team_rocket_supporter(c)]
    count = 0
    if pool:
        picks = await ctx.discard_from_hand(
            len(pool), minimum=0, predicate=_team_rocket_supporter,
            prompt="Discard any number of Team Rocket Supporter cards (60 each)")
        count = len(picks or [])
    if count:
        await ctx.deal_damage(60 * count)


card = PokemonCardDef(
    guid="1340b907-387c-51a0-89b8-28e661cc1ecc",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsHonchkrow.Name",
    display_name="Team Rocket's Honchkrow",
    searchable_by=["Team Rocket's Honchkrow", "Stage 1", "TeamRocketsHonchkrow"],
    subtypes=["Stage 1"],
    collector_number=127,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMurkrow.Name",
    family_id=198,
    abilities=[
        Attack(title="Rocket Feathers",
               game_text="You may discard any number of Supporter cards that have \"Team Rocket\" in their name from your hand, and this attack does 60 damage for each card you discarded in this way.",
               cost={PokemonTypes.COLORLESS: 2},
               damage=60, damage_operator="x", effect=rocket_feathers),
        Attack(title="Hammer In", game_text="",
               cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=100),
    ],
)
