"""Jynx (SV06 46 -- JP SV6 028; English TWM/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def inviting_kiss(ctx):
    benched = None
    if effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()) > 0:
        picks = await ctx.search_deck(is_basic_pokemon, count=1, minimum=0, prompt="Choose a Basic Pokémon to put onto your Bench.")
        for card in picks:
            if await ctx.bench_pokemon(card):
                benched = card
    await ctx.shuffle_deck()
    pool = list(ctx.attached_energies(ctx.attacker))
    if benched is not None and pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to move to the new Benched Pokémon")
        if picks:
            await ctx.move_energy(picks[0], benched)


card = PokemonCardDef(
    guid="74c37a15-3815-5113-a2b9-cf4dba4944fa",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=238,
    abilities=[
        Attack(
            title="Inviting Kiss",
            game_text="Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck. If you put any Pokémon onto your Bench in this way, move an Energy from this Pokémon to the new Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=inviting_kiss,
        ),
        Attack(
            title="Icy Snow",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
    ],
)
