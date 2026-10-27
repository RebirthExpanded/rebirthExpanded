"""Jirachi (SV07 98 -- JP SVI 039; English SCR/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def swelling_wish(ctx):
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card to attach")
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon") if picks else None
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="0c76740a-1aa3-5e7e-ad66-338c7cc3c95c",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=385,
    abilities=[
        Attack(
            title="Swelling Wish",
            game_text="Attach a Basic Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=swelling_wish,
        ),
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
