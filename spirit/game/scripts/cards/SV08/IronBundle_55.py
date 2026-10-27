"""Iron Bundle (SV08 55 -- JP SV8 031; English SSP/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import effective_retreat_cost


async def gusting_collision(ctx):
    d = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, d) if d is not None else 0
    amount = max(0, 200 - 50 * cost)
    if amount:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="88cbbe01-500a-55f5-aacb-ae3cee722cd2",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBundle.Name",
    display_name="Iron Bundle",
    searchable_by=["Iron Bundle", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=55,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=991,
    abilities=[
        Attack(
            title="Gusting Collision",
            game_text="This attack does 50 less damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            damage_operator="-",
            effect=gusting_collision,
        ),
    ],
)
