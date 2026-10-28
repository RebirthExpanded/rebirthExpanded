"""Orthworm (SV4 138 -- JP SV3a 049; English PAR/138). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def punch_and_draw(ctx):
    await ctx.deal_damage()
    await ctx.draw_cards(2)


def _thin_deck(ctx) -> bool:
    return len(ctx.deck()) <= 3


card = PokemonCardDef(
    guid="298a169e-ff39-5ac9-8a29-2df839b81152",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orthworm.Name",
    display_name="Orthworm",
    searchable_by=["Orthworm", "Basic"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=968,
    abilities=[
        Attack(
            title="Punch and Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=punch_and_draw,
        ),
        Attack(
            title="Crunch-Time Rush",
            game_text="If there are 3 or fewer cards in your deck, this attack does 150 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_thin_deck, 150),
        ),
    ],
)
