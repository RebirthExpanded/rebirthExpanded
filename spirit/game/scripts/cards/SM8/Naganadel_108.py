"""Naganadel (SM - Lost Thunder 108/214 -- JP SM8 048/095).

Stage 1 Psychic Pokemon, Ultra Beast, evolves from Poipole. HP 130,
weakness Psychic x2, retreat 1.

  Ability  Charging Up  Once during your turn (before your attack), you may
                        attach a basic Energy card from your discard pile to
                        this Pokemon.
  Turning Point  [CCC] 80+  If you have exactly 3 Prize cards remaining,
                            this attack does 80 more damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, count_prizes_remaining
from spirit.game.card_effects.support_common import attach_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


_prizes_left = count_prizes_remaining("mine")


def _charging_up_condition(board, player_id, pokemon) -> bool:
    return requires_discard(is_basic_energy_card, 1)(board, player_id)


card = PokemonCardDef(
    guid="817db598-9454-51e8-8cf6-0a4246da305f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Naganadel.Name",
    display_name="Naganadel",
    searchable_by=['Naganadel', 'Stage 1', 'Ultra Beast', 'Naganadel'],
    subtypes=['Stage 1', 'Ultra Beast'],
    collector_number=108,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    family_id=803,
    abilities=[
        Ability(
            title="Charging Up",
            game_text="Once during your turn (before your attack), you may attach a basic Energy card from your discard pile to this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_charging_up_condition,
            effect=attach_from_discard(
                is_basic_energy_card, count=1, target="self",
                prompt="Choose a basic Energy card to attach to this Pokémon"),
        ),
        Attack(title="Turning Point", game_text="If you have exactly 3 Prize cards remaining, this attack does 80 more damage.",
               cost={PokemonTypes.COLORLESS: 3}, damage=80, damage_operator="+",
               effect=bonus_if(lambda ctx: _prizes_left(ctx) == 3, 80)),
    ],
)
