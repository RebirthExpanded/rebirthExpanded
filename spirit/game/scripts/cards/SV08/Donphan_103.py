"""Donphan (SV08 103 -- JP SV8 065; English SSP/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


async def guarded_rolling(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    n = min(2, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy to discard from this Pokémon")
        await ctx.discard_cards(picks)
    await pc.apply_protection(ctx, reduce=100)


card = PokemonCardDef(
    guid="e22eb04a-86e7-5a33-b37a-a4627f84ead9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="Knock Flat",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=ac.ignore_effects_attack(),
        ),
        Attack(
            title="Guarded Rolling",
            game_text="Discard 2 Energy from this Pokémon. During your opponent's next turn, this Pokémon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=guarded_rolling,
        ),
    ],
)
