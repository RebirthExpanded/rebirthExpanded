"""Heat Rotom (SV10 43 -- JP SV10 021; English DRI/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import full_stack, is_pokemon_tool


async def gadget_show(ctx):
    """30 for each Pokemon Tool attached to all of your Pokemon."""
    tools = sum(1 for p in ctx.my_pokemon_in_play()
                for c in full_stack(p) if c is not p and is_pokemon_tool(c))
    if tools:
        await ctx.deal_damage(30 * tools)


card = PokemonCardDef(
    guid="68f0ad43-4a6c-5608-8501-cb94ba286275",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatRotom.Name",
    display_name="Heat Rotom",
    searchable_by=["Heat Rotom", "Basic"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=479,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pokémon Tool attached to all of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=gadget_show,
        ),
    ],
)
