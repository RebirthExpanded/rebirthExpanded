"""Throh (ZSV10PT5 50 -- JP SV11B 053; English BLK/128, BLK/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import effective_retreat_cost


async def shoulder_throw(ctx):
    d = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, d) if d is not None else 0
    amount = max(0, 120 - 30 * cost)
    if amount:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="cb6161f4-3ee1-5ddb-bcb6-3499428630c7",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(
            title="Shoulder Throw",
            game_text="This attack does 30 less damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="-",
            effect=shoulder_throw,
        ),
    ],
)
