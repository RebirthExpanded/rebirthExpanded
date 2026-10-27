"""Tornadus (RSV10PT5 78 -- JP SV11W 078; English SVP/210, WHT/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def wrapped_in_wind(ctx):
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card to attach to this Pokémon")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


async def hurricane(ctx):
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e)]
    bench = ctx.my_bench()
    if not pool or not bench or ctx.attacker in ctx.knockouts:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy to move")
    dest = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move it to") if picks else None
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


card = PokemonCardDef(
    guid="98e8c13b-b00a-5d42-a815-9e68069bc77d",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus", "Basic"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=641,
    abilities=[
        Attack(
            title="Wrapped in Wind",
            game_text="Attach a Basic Energy card from your hand to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=wrapped_in_wind,
        ),
        Attack(
            title="Hurricane",
            game_text="Move a Basic Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=hurricane,
        ),
    ],
)
