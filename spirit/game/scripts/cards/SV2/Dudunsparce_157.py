"""Dudunsparce (SV2 157 -- JP SV2P 057; English PAL/157, PAL/229). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions

from spirit.game.session.effects import full_stack


async def dig_away_flash(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts:
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
    me = ctx.attacker
    if me not in ctx.knockouts and ctx.my_bench():
        await ctx.shuffle_into_deck(full_stack(me), ctx.player_id)


card = PokemonCardDef(
    guid="b78eca56-0257-580f-a04c-6ea66ad3d7a3",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dudunsparce.Name",
    display_name="Dudunsparce",
    searchable_by=["Dudunsparce", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=157,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    family_id=206,
    abilities=[
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Dig Away Flash",
            game_text="Your opponent's Active Pokémon is now Paralyzed. Shuffle this Pokémon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=dig_away_flash,
        ),
    ],
)
