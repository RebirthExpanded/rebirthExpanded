"""Mismagius (ME2PT5 86 -- JP M2a 068; English ASC/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def assassins_magic(ctx):
    d = ctx.opponent_active()
    afflicted = d is not None and bool(d.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if afflicted and bench:
        target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon to place 6 damage counters on")
        if target is not None:
            await ctx.deal_damage(60, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="3422d7c9-4e66-543f-bbea-ad8ed6937cfd",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=86,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Attack(
            title="Assassin's Magic",
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, place 6 damage counters on 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=assassins_magic,
        ),
    ],
)
