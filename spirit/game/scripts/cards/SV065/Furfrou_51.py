"""Furfrou (SV065 51 -- JP SV6a 051; English SFA/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def energy_assist(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card to attach")
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon") if picks else None
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="21c2b1d9-6815-5b74-9de8-e26ce0dcb081",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=["Furfrou", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach a Basic Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=energy_assist,
        ),
    ],
)
