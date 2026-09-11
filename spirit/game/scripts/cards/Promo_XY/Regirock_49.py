"""Regirock (XY Black Star Promos XY49 -- JP XY-P promo).

Basic Fighting Pokemon. HP 110, weakness Grass x2, retreat 3.

  Ancient Trait  Ω Barrier  Whenever your opponent plays a Trainer card
                            (excluding Pokemon Tools and Stadium cards),
                            prevent all effects of that card done to this
                            Pokemon.
  Land Maker  [F]        Put 2 Stadium cards from your discard pile into
                         your hand.
  Stone Edge  [FFFC] 80+  Flip a coin. If heads, this attack does 40 more
                          damage.

Ω Barrier is Electrike's, shared through OmegaBarrierPassive. Land Maker
takes up to 2 Stadiums -- with one there it takes the one, with none the
attack does nothing.
"""

from spirit.game.attributes import (AbilityTypes, PokemonStage, PokemonTypes,
                                    Rarities)
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import OmegaBarrierPassive
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_stadium_card

card = PokemonCardDef(
    guid="d9c5cdc6-4c48-5d10-8e30-edcc0f7f9cc4",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Ability(
            title="Ω Barrier",
            game_text="Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.",
            ability_type=AbilityTypes.ANCIENT_TRAIT,
            passive=OmegaBarrierPassive(),
        ),
        Attack(
            title="Land Maker",
            game_text="Put 2 Stadium cards from your discard pile into your hand.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=recover_from_discard(
                is_stadium_card, count=2, minimum=1,
                prompt="Choose up to 2 Stadium cards to put into your hand."),
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=flip_bonus(40),
        ),
    ],
)
