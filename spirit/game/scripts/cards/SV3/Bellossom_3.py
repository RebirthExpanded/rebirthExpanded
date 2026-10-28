"""Bellossom (SV3 3 -- JP SV3 003; English OBF/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def powerful_dance(ctx):
    n = len(ctx.attached_energies(ctx.attacker))
    heads = sum(1 for r in await ctx.flip_coins(n, "Powerful Dance") if r) if n else 0
    if heads:
        await ctx.deal_damage(90 * heads)


card = PokemonCardDef(
    guid="f0fdd8f2-7eec-5b4f-8206-d0272af6a534",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name",
    display_name="Bellossom",
    searchable_by=["Bellossom", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Powerful Dance",
            game_text="Flip a coin for each Energy attached to this Pokémon. This attack does 90 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=90,
            damage_operator="x",
            effect=powerful_dance,
        ),
    ],
)
