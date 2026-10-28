"""Vivillon (SV1 10 -- JP SV1V 005; English SVI/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


_CHOICES = [("Asleep", SpecialConditions.ASLEEP), ("Burned", SpecialConditions.BURNED),
            ("Confused", SpecialConditions.CONFUSED), ("Paralyzed", SpecialConditions.PARALYZED),
            ("Poisoned", SpecialConditions.POISONED)]


async def miracle_powder(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Miracle Powder")
    target = ctx.opponent_active()
    if not (results and results[0]) or target is None or target in ctx.knockouts:
        return
    index = await ctx.choose("Choose a Special Condition", [label for label, _ in _CHOICES])
    if isinstance(index, int) and 0 <= index < len(_CHOICES):
        await ctx.apply_special_condition(target, _CHOICES[index][1])


card = PokemonCardDef(
    guid="86414f5a-545f-5e98-ba4e-bef12364e70e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose a Special Condition. Your opponent's Active Pokémon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=miracle_powder,
        ),
        Attack(
            title="Bug Buzz",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
