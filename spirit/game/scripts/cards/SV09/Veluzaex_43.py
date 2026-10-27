"""Veluza ex (SV09 43 -- JP SVP 165; English JTG/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def purging_strike(ctx):
    hand = list(ctx.hand())
    if hand and await ctx.ask_yes_no("Discard your hand for 120 more damage?"):
        await ctx.discard_cards(hand)
        await ctx.deal_damage(240)
    else:
        await ctx.deal_damage(120)


card = PokemonCardDef(
    guid="6ef85954-ed3c-5c01-aa0e-cb3c38490873",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluzaex.Name",
    display_name="Veluza ex",
    searchable_by=["Veluza ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=43,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=976,
    abilities=[
        Attack(
            title="Razor Fin",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Purging Strike",
            game_text="You may discard your hand. If you discarded any cards in this way, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=purging_strike,
        ),
    ],
)
