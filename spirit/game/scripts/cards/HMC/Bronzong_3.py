"""Bronzong (JP XY Hyper Metal Chain Deck 60 -- HMC 003/018; English print
XY - Phantom Forces 61/119).

Stage 1 Metal Pokemon, evolves from Bronzor. HP 90, weakness Fire x2,
resistance Psychic -20, retreat 3.

  Ability  Metal Links  Once during your turn (before your attack), you may
                        attach a [M] Energy card from your discard pile to
                        1 of your Benched Pokemon.
  Hammer In  [MMC] 60

The deck's engine. Only a Benched Pokemon may receive the Energy, and the
ability is not offered with no [M] Energy card in the discard pile or no
Benched Pokemon to take it.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import (attach_from_discard,
                                                     requires_discard)
from spirit.game.card_effects.trainers import is_metal_energy_card
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


def _benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)


def _metal_links_condition(board, player_id, pokemon) -> bool:
    if not requires_discard(is_metal_energy_card, 1)(board, player_id):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


card = PokemonCardDef(
    guid="4eff4367-1250-5fd1-bd7c-f5b9eee7841a",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="HMC",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=437,
    abilities=[
        Ability(
            title="Metal Links",
            game_text="Once during your turn (before your attack), you may attach a [M] Energy card from your discard pile to 1 of your Benched Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_metal_links_condition,
            effect=attach_from_discard(
                is_metal_energy_card, count=1, target=_benched,
                prompt="Choose a [M] Energy card to attach to a Benched Pokémon"),
        ),
        Attack(title="Hammer In", game_text="",
               cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1}, damage=60),
    ],
)
