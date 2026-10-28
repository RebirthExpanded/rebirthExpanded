"""Hitmonlee (SV035 106 -- JP SV2a 106; English MEW/106). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def twister_kick(ctx):
    await ac.damage_all_opponents(10)(ctx)
    bench = ctx.my_bench()
    if bench and ctx.attacker not in ctx.knockouts:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="a22c5b38-a4fc-59cf-a155-30ca1f1d53d5",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name",
    display_name="Hitmonlee",
    searchable_by=["Hitmonlee", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=236,
    abilities=[
        Attack(
            title="Twister Kick",
            game_text="This attack does 10 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=twister_kick,
        ),
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
        ),
    ],
)
