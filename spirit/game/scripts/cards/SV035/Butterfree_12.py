"""Butterfree (SV035 12 -- JP SV2a 012; English MEW/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import full_stack


async def bye_bye_flight(ctx):
    bench = [p for p in ctx.opponent_bench() if not ctx.effects_blocked(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is None:
        return
    await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)
    if ctx.my_bench():
        await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)


card = PokemonCardDef(
    guid="38351891-c9db-5776-90e2-f1f18804205f",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=su.gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Bye-Bye Flight",
            game_text="Choose 1 of your opponent's Benched Pokémon. Shuffle that Pokémon and all attached cards into their deck, and then shuffle this Pokémon and all attached cards into your deck. If your opponent has no Benched Pokémon, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=bye_bye_flight,
        ),
    ],
)
