"""Eiscue (SV2 48 -- JP SV2P 019; English PAL/205, PAL/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def frigid_block(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool:
        await ctx.discard_cards(pool)
    await pc.apply_protection(ctx, reduce=100)


card = PokemonCardDef(
    guid="29392d33-5184-5c33-abbd-b22470dd5b28",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Frigid Block",
            game_text="Discard all Energy from this Pokémon. During your opponent's next turn, this Pokémon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            effect=frigid_block,
        ),
    ],
)
