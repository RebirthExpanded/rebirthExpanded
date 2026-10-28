"""Iron Moth (SV4 28 -- JP SV4M 012; English PAR/187, PAR/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def thermal_reactor(ctx):
    me = ctx.source
    pool = [e for p in ctx.my_pokemon_in_play() if p is not me for e in ctx.attached_energies(p)
            if is_energy_of_type(e, PokemonTypes.FIRE)]
    if not pool or not await ctx.ask_yes_no("Use Thermal Reactor?"):
        return
    picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Choose any amount of Fire Energy to move to this Pokémon")
    for e in picks:
        await ctx.move_energy(e, me)


card = PokemonCardDef(
    guid="dfe86a3c-6935-57af-b6f7-f3fecefbc738",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronMoth.Name",
    display_name="Iron Moth",
    searchable_by=["Iron Moth", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=28,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=994,
    abilities=[
        Ability(
            title="Thermal Reactor",
            game_text="Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may move any amount of Fire Energy from your other Pokémon to it.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            effect=thermal_reactor,
        ),
        Attack(
            title="Heat Ray",
            game_text="During your next turn, this Pokémon can't use Heat Ray.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
