"""Skarmory (SV10 141 -- JP SV10 074; English DRI/141). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.session.passives import Passive, carrier_pokemon


async def roost(ctx):
    await ctx.heal(50, ctx.attacker)
    ctx.add_passive_through_own_next_turn(
        ctx.attacker, pc.no_retreat_passive(lambda p, c: p is carrier_pokemon(c)))


card = PokemonCardDef(
    guid="42d07482-afa0-5290-9dbf-3e647d0c1d1b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=227,
    abilities=[
        Attack(
            title="Roost",
            game_text="Heal 50 damage from this Pokémon. During your next turn, this Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=roost,
        ),
        Attack(
            title="Metal Claw",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
