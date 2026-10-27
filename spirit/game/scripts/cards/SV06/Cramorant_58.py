"""Cramorant (SV06 58 -- JP SV5a 025; English TWM/176, TWM/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def spit_shot(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool:
        await ctx.discard_cards(pool)
    await ac.snipe_attack(120, pool="any")(ctx)


card = PokemonCardDef(
    guid="82dbdbeb-fb0b-5b86-b92d-95db922c7a1e",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cramorant.Name",
    display_name="Cramorant",
    searchable_by=["Cramorant", "Basic"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=845,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Spit Shot",
            game_text="Discard all Energy from this Pokémon. This attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=spit_shot,
        ),
    ],
)
