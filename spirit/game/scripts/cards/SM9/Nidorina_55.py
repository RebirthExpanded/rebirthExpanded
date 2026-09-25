"""Nidorina (SM - Team Up 55/181 -- JP SM9 040/095).

Stage 1 Psychic Pokemon, evolves from Nidoran♀. HP 90, weakness Psychic
x2, retreat 2.

  Family Rescue  [C]      Shuffle 5 [P] Pokemon from your discard pile
                          into your deck.
  Bite           [CC] 30

The Japanese text has the 5 cards shown to the opponent first. With fewer
than 5 Psychic Pokemon in the discard pile, all of them go back.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_card


def _psychic_pokemon(card) -> bool:
    return (is_pokemon_card(card)
            and PokemonTypes.PSYCHIC.value in (card.get_attribute(AttrID.POKEMON_TYPES) or []))


async def family_rescue(ctx):
    candidates = [c for c in ctx.discard_pile() if _psychic_pokemon(c)]
    if not candidates:
        return
    take = min(5, len(candidates))
    picks = candidates if len(candidates) <= 5 else await ctx.choose_cards(
        candidates, take, minimum=take,
        prompt="Choose 5 Psychic Pokémon to shuffle into your deck.",
    )
    if not picks:
        return
    await ctx.reveal_cards(picks, to_player=ctx.opponent_id)
    await ctx.shuffle_into_deck(picks)


card = PokemonCardDef(
    guid="497008ab-9d9d-51a4-8d81-0bd955ad8495",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    display_name="Nidorina",
    searchable_by=["Nidorina", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranFemale.Name",
    family_id=29,
    abilities=[
        Attack(title="Family Rescue",
               game_text="Shuffle 5 Psychic Pokémon from your discard pile into your deck.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=family_rescue),
        Attack(title="Bite", game_text="", cost={PokemonTypes.COLORLESS: 2}, damage=30),
    ],
)
