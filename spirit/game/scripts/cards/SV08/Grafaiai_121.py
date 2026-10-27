"""Grafaiai (SV08 121 -- JP SV8 074; English SSP/121). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_card


async def mischievous_painting(ctx):
    pool = [c for c in ctx.discard_pile(ctx.opponent_id) if is_energy_card(c)]
    mons = ctx.opponent_pokemon_in_play()
    if not pool or not mons:
        return
    picks = await ctx.choose_cards(pool, min(3, len(pool)), minimum=0, prompt="Attach up to 3 Energy cards to your opponent's Pokémon")
    for card in picks:
        target = await ctx.choose_pokemon(mons, "Choose 1 of your opponent's Pokémon")
        if target is not None:
            await ctx.attach_energy(card, target)


async def energized_graffiti(ctx):
    n = sum(len(ctx.attached_energies(p)) for p in ctx.opponent_pokemon_in_play())
    if n:
        await ctx.deal_damage(40 * n)


card = PokemonCardDef(
    guid="47fbaddd-fc3d-565c-afaf-7a22fdb9a9d5",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grafaiai.Name",
    display_name="Grafaiai",
    searchable_by=["Grafaiai", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    family_id=944,
    abilities=[
        Attack(
            title="Mischievous Painting",
            game_text="Attach up to 3 Energy cards from your opponent's discard pile to their Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mischievous_painting,
        ),
        Attack(
            title="Energized Graffiti",
            game_text="This attack does 40 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            damage_operator="x",
            effect=energized_graffiti,
        ),
    ],
)
