"""Drifblim (SV1 90 -- JP SV1S 030; English PAF/156, SVI/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def curse_spreading(ctx):
    for _ in range(8):
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            return
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to put a damage counter on")
        if target is None:
            return
        await ctx.deal_damage(10, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="2310c054-b955-5c63-950e-a96008b1b4f1",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Attack(
            title="Gust",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Curse Spreading",
            game_text="Put 8 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=curse_spreading,
        ),
    ],
)
