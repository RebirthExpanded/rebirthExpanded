"""Bronzong (ME2 72 -- JP M2 060; English PFL/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import full_stack, is_pokemon_tool


async def tool_drop(ctx):
    tools = sum(1 for pid in ctx.board.player_ids for p in ctx.board.pokemon_in_play(pid)
                for c in full_stack(p) if c is not p and is_pokemon_tool(c))
    if tools:
        await ctx.deal_damage(40 * tools)


card = PokemonCardDef(
    guid="8c847431-8618-54e8-9f00-9444b5f47832",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(3),
        ),
        Attack(
            title="Tool Drop",
            game_text="This attack does 40 damage for each Pokémon Tool attached to all Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=tool_drop,
        ),
    ],
)
