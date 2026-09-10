"""Pidgeotto (SM - Team Up 123/181).

Stage 1 Colorless Pokemon. HP 60, weakness Lightning x2, resistance
Fighting -20, retreat 1.

  Ability  Air Mail  Once during your turn (before your attack), you may
                     look at the top 2 cards of your deck and put 1 of them
                     into your hand. Put the other card on the bottom of
                     your deck.

  Gust [CC] 30

Air Mail is Drakloak's Recon Directive word for word, so the effect moved
to card_effects/pokemon.look_at_top_2_keep_1 and both cards point at it.
Nothing is revealed: neither card says to.

The SM-era resistance is -20, not the -30 the definition defaults to.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import look_at_top_2_keep_1
from spirit.game.card_effects.support_common import requires_deck

card = PokemonCardDef(
    guid="85ab4205-4f96-5aff-9dbd-63314f081266",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    display_name="Pidgeotto",
    searchable_by=["Pidgeotto", "Stage 1", "Pidgeotto"],
    subtypes=["Stage 1"],
    collector_number=123,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    family_id=16,
    abilities=[
        Ability(
            title="Air Mail",
            game_text=(
                "Once during your turn (before your attack), you may look at "
                "the top 2 cards of your deck and put 1 of them into your "
                "hand. Put the other card on the bottom of your deck."
            ),
            activation=Activations.ONCE_PER_TURN,
            # Nothing to look at, nothing to do: not offered on an empty deck.
            condition=requires_deck(),
            effect=look_at_top_2_keep_1,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
