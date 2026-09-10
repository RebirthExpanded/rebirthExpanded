"""Sableye (SM - Guardians Rising 80/145 -- JP SM2L 031/050).

Basic Darkness. HP 60, no weakness, no resistance, retreat 1.

  Limitation  [D]     Your opponent can't play any Supporter cards from
                      their hand during their next turn.
  Scratch     [C] 20

A one-attack lock, the narrowest of the family: Vileplume names Items,
Umbreon & Darkrai-GX names Trainers, this one names Supporters only, so
their Items and Stadiums keep working.

Limitation deals no damage at all, so the Attack carries none and the lock
is the whole of it.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_supporter_card


async def limitation(ctx):
    """No Supporters from their hand next turn."""
    ctx.lock_plays(ctx.opponent_id, is_supporter_card)


card = PokemonCardDef(
    guid="ac05d338-0f27-500a-9fb4-3338373b02a4",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title="Limitation",
            game_text="Your opponent can't play any Supporter cards from their hand during their next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=limitation,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
