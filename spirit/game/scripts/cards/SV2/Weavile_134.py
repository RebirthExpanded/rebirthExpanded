"""Weavile (SV2 134 -- JP SV2D 051; English PAF/183, PAL/134). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_basic_pokemon_in_play


async def assaulting_hunt(ctx):
    pool = [p for p in ctx.opponent_bench() if is_basic_pokemon_in_play(p)]
    if not pool or not await ctx.ask_yes_no("Use Assaulting Hunt?"):
        return
    target = await ctx.choose_pokemon(pool, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="9abbbaa2-50a6-5eee-9fe5-05f37409a656",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Ability(
            title="Assaulting Hunt",
            game_text="Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may switch in 1 of your opponent's Benched Basic Pokémon to the Active Spot.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            effect=assaulting_hunt,
        ),
        Attack(
            title="Slashing Claw",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
