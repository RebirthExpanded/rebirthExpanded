"""Landorus (ME3 41 -- JP M3 040; English POR/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def rock_tumble(ctx):
    await ctx.deal_damage(ignore_resistance=True)


async def screw_knuckle(ctx):
    await ctx.deal_damage()
    pool = ctx.attached_energies(ctx.attacker)
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="3135b0ba-1746-5e41-a86b-cfe914468e3c",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus", "Basic"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=645,
    abilities=[
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            effect=rock_tumble,
        ),
        Attack(
            title="Screw Knuckle",
            game_text="Put an Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=screw_knuckle,
        ),
    ],
)
