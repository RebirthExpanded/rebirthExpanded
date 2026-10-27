"""Smeargle (ME2 80 -- JP M2 068; English PFL/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def energizing_sketch(ctx):
    heads = sum(1 for r in await ctx.flip_coins(3, "Energizing Sketch") if r)
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not heads or not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, min(heads, len(pool)), minimum=0,
                                   prompt=f"Choose up to {heads} Basic Energy cards to attach to your Benched Pokémon")
    for card in picks:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="db7451b4-fc7d-599e-b05a-770c793566b5",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Attack(
            title="Energizing Sketch",
            game_text="Flip 3 coins. Attach an amount of Basic Energy up to the number of heads from your discard pile to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energizing_sketch,
        ),
        Attack(
            title="Hook",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
