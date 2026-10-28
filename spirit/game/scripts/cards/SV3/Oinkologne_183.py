"""Oinkologne (SV3 183 -- JP SVD 103; English OBF/183). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def high_impact_kick(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "High-Impact Kick")
    if results and not results[0]:
        await ctx.deal_damage(60, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="57b94404-e360-5147-9985-cf79c9962937",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name",
    display_name="Oinkologne",
    searchable_by=["Oinkologne", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=183,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    family_id=915,
    abilities=[
        Attack(
            title="Confounding Cologne",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="High-Impact Kick",
            game_text="Flip a coin. If tails, this Pokémon also does 60 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=high_impact_kick,
        ),
    ],
)
