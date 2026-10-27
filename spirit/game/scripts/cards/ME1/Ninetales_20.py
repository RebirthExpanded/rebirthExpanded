"""Ninetales (ME1 20 -- JP M1L 011; English MEG/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import TRAINER_EFFECTS_BY_GUID, unimplemented
from spirit.game.session.effects import is_supporter_card


async def supernatural_shapeshifter(ctx):
    top = list(ctx.deck_top(1))
    if not top:
        return
    card = top[0]
    await ctx.discard_cards([card])
    if not is_supporter_card(card):
        return
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    if effect is not None and effect is not unimplemented:
        await effect(ctx)


card = PokemonCardDef(
    guid="c96cb2d3-c6e9-563d-baef-2b9887677074",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Supernatural Shapeshifter",
            game_text="Discard the top card of your deck, and if that card is a Supporter card, use the effect of that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=supernatural_shapeshifter,
        ),
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
