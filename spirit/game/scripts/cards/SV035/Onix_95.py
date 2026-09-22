"""Onix (SV - 151 095/165 -- JP SV2a 095/165, the art here).

Basic Fighting Pokemon. HP 120, weakness Grass x2, retreat 4.

  Land Crush     [FC]   80x  Discard the top 5 cards of your deck. This
                             attack does 80 damage for each Pokemon you
                             discarded that has a Retreat Cost of 4.
  Heavy Impact   [FCC]  100

The count is the PRINTED Retreat Cost of the discarded cards -- they are
in the deck, where no passive reduces anything.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_card

MILL = 5
PER_MATCH = 80
RETREAT_COST = 4


async def land_crush(ctx):
    top = ctx.deck_top(MILL)
    await ctx.discard_cards(top)
    matches = sum(
        1 for card in top
        if is_pokemon_card(card)
        and int(card.get_attribute(AttrID.RETREAT_COST) or 0) == RETREAT_COST)
    if matches:
        await ctx.deal_damage(PER_MATCH * matches)


card = PokemonCardDef(
    guid="376fc03b-6572-543a-80bd-464a2fd66036",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="SV035",
    regulation_mark="F",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Land Crush",
            game_text="Discard the top 5 cards of your deck. This attack does 80 damage for each Pokémon you discarded that has a Retreat Cost of 4.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="x",
            effect=land_crush,
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
