"""Landorus (SV08 110 -- JP SV7a 030; English SSP/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_card


async def fist_of_focus(ctx):
    await ctx.deal_damage()
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if pool and ctx.attacker not in ctx.knockouts:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy card to attach to this Pokémon")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)


async def buster_swing(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="1d09a596-04e0-5b1e-a9f5-867b79541729",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus", "Basic"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=645,
    abilities=[
        Attack(
            title="Fist of Focus",
            game_text="Attach an Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=fist_of_focus,
        ),
        Attack(
            title="Buster Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=buster_swing,
        ),
    ],
)
