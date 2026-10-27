"""Grafaiai (ME1 92 -- JP M1L 044; English MEG/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


_CHOICES = [("Asleep", SpecialConditions.ASLEEP), ("Burned", SpecialConditions.BURNED),
            ("Confused", SpecialConditions.CONFUSED), ("Paralyzed", SpecialConditions.PARALYZED),
            ("Poisoned", SpecialConditions.POISONED)]


async def miraculous_paint(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Miraculous Paint")
    target = ctx.opponent_active()
    if not (results and results[0]) or target is None or target in ctx.knockouts:
        return
    index = await ctx.choose("Choose a Special Condition", [label for label, _ in _CHOICES])
    if isinstance(index, int) and 0 <= index < len(_CHOICES):
        await ctx.apply_special_condition(target, _CHOICES[index][1])


card = PokemonCardDef(
    guid="6f53e77f-a9dd-550e-bde9-974c97ea2a96",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grafaiai.Name",
    display_name="Grafaiai",
    searchable_by=["Grafaiai", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    family_id=944,
    abilities=[
        Attack(
            title="Miraculous Paint",
            game_text="Flip a coin. If heads, choose a Special Condition. Your opponent's Active Pokémon is now affected by that Special Condition.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=miraculous_paint,
        ),
    ],
)
