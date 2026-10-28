"""Palkia (SV4 40 -- JP SV3a 008; English PAR/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def strafe(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench and ctx.attacker not in ctx.knockouts and await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


def _more_left(ctx) -> bool:
    return ac.count_prizes_remaining("mine")(ctx) > ac.count_prizes_remaining("opponent")(ctx)


card = PokemonCardDef(
    guid="cc88dfa6-3a83-5a4a-892c-2818beb9ec44",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Attack(
            title="Teleportation Burst",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=strafe,
        ),
        Attack(
            title="Prize Count",
            game_text="If you have more Prize cards remaining than your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_more_left, 80),
        ),
    ],
)
