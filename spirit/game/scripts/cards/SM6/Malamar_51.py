"""Malamar (SM - Forbidden Light 51/131 -- JP SM6 037/094).

Stage 1 Psychic Pokemon, evolves from Inkay. HP 90, weakness Psychic x2,
retreat 2.

  Ability  Psychic Recharge  Once during your turn (before your attack), you
                             may attach a [P] Energy card from your discard
                             pile to 1 of your Benched Pokemon.
  Psychic Sphere  [PPC] 60

Not offered with no [P] Energy card in the discard pile or an empty Bench
(Bronzong's Metal Links shape).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import attach_from_discard, requires_discard
from spirit.game.session.effects import is_energy_of_type
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


def _psychic_energy_card(card) -> bool:
    return is_energy_of_type(card, PokemonTypes.PSYCHIC)


def _benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)


def _psychic_recharge_condition(board, player_id, pokemon) -> bool:
    if not requires_discard(_psychic_energy_card, 1)(board, player_id):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


card = PokemonCardDef(
    guid="08cf036c-3c51-5031-b857-56d3b0c59b45",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=['Malamar', 'Stage 1', 'Malamar'],
    subtypes=['Stage 1'],
    collector_number=51,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Ability(
            title="Psychic Recharge",
            game_text="Once during your turn (before your attack), you may attach a Psychic Energy card from your discard pile to 1 of your Benched Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_psychic_recharge_condition,
            effect=attach_from_discard(
                _psychic_energy_card, count=1, target=_benched,
                prompt="Choose a Psychic Energy card to attach to a Benched Pokémon"),
        ),
        Attack(title="Psychic Sphere", game_text="",
               cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=60),
    ],
)
