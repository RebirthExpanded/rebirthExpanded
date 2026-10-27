"""Snorlax (SV06 136 -- JP SV5a 051; English TWM/136). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_card


async def but_first_food(ctx):
    pool = [c for c in ctx.hand() if is_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy card to attach to this Pokémon")
    if picks and await ctx.attach_energy(picks[0], ctx.attacker):
        await ctx.heal(60, ctx.attacker)


card = PokemonCardDef(
    guid="6d932d64-3d18-5cba-be03-a440f4dcab7e",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Attack(
            title="But First, Food",
            game_text="Attach an Energy card from your hand to this Pokémon. If you do, heal 60 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=but_first_food,
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.COLORLESS: 5},
            damage=160,
        ),
    ],
)
