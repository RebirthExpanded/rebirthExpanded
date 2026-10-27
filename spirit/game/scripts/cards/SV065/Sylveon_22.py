"""Sylveon (SV065 22 -- JP SV6a 022; English SFA/22, SVP/172). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import full_stack


async def mystical_return(ctx):
    results = await ctx.flip_coins(1, "Mystical Return")
    bench = [p for p in ctx.opponent_bench() if not ctx.effects_blocked(p)]
    if not (results and results[0]) or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon to shuffle into their deck")
    if target is not None:
        await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)


card = PokemonCardDef(
    guid="c1e5e6a2-4555-5582-9620-f7b2e9b31073",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Mystical Return",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Benched Pokémon. Shuffle that Pokémon and all attached cards into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=mystical_return,
        ),
        Attack(
            title="Disarming Voice",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
