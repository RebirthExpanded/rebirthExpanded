"""Slakoth (SV08 145 -- JP SV8 082; English SSP/145, SSP/212). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.session.passives import Passive, carrier_pokemon


async def take_it_easy(ctx):
    await ctx.heal(60, ctx.attacker)
    ctx.add_passive_through_own_next_turn(
        ctx.attacker, pc.no_retreat_passive(lambda p, c: p is carrier_pokemon(c)))


card = PokemonCardDef(
    guid="fd245649-4074-5982-b00b-39142f3e6e1d",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Take It Easy",
            game_text="Heal 60 damage from this Pokémon. During your next turn, this Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=take_it_easy,
        ),
    ],
)
