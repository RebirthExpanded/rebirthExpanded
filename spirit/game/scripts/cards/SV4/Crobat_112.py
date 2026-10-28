"""Crobat (SV4 112 -- JP SV4K 046; English PAR/112). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_item_card, is_supporter_card


async def echoing_madness(ctx):
    await ctx.deal_damage()
    index = await ctx.choose("Choose the cards your opponent can't play", ["Item cards", "Supporter cards"])
    ctx.lock_plays(ctx.opponent_id, is_supporter_card if index == 1 else is_item_card)


card = PokemonCardDef(
    guid="4a2d023e-756d-5447-b7ce-007d8d890597",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=112,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Echoing Madness",
            game_text="Choose Item cards or Supporter cards. During your opponent's next turn, they can't play any of the chosen cards from their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=echoing_madness,
        ),
        Attack(
            title="Cutting Wind",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)
