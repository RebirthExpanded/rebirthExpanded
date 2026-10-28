"""Tentacruel (SV035 73 -- JP SV2a 073; English MEW/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def tentacular_panic(ctx):
    results = []
    while True:
        r = await ctx.flip_coins(1, "Tentacular Panic")
        heads = bool(r and r[0])
        results.append(heads)
        if not heads:
            break
    n = sum(1 for r in results if r)
    if n:
        await ctx.deal_damage(90 * n)
    elif results and not results[0]:
        d = ctx.opponent_active()
        if d is not None:
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="4ef27e0f-3daa-59c0-8323-eaa1ae70912a",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=72,
    abilities=[
        Attack(
            title="Poisonous Whip",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Tentacular Panic",
            game_text="Flip a coin until you get tails. This attack does 90 damage for each heads. If the first flip is tails, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=tentacular_panic,
        ),
    ],
)
