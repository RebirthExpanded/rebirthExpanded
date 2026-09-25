"""Nidoqueen (SM - Team Up 56/181 -- JP SM9 041/095).

Stage 2 Psychic Pokemon, evolves from Nidorina. HP 160, weakness Psychic
x2, retreat 3.

  Ability  Queen's Call  Once during your turn (before your attack), you may
                         search your deck for a Pokemon that isn't a
                         Pokemon-GX or Pokemon-EX, reveal it, and put it into
                         your hand. Then, shuffle your deck.
  Power Lariat  [CCC] 10+  This attack does 50 more damage for each
                           Evolution Pokemon on your Bench.

Pokemon-EX is the uppercase XY/BW mechanic; a Scarlet & Violet Pokemon ex
is not one and may be searched.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, subtypes_for
from spirit.game.session.effects import is_evolution_pokemon, is_pokemon_card


def _queens_call_target(card) -> bool:
    subtypes = subtypes_for(card.archetype_id)
    return is_pokemon_card(card) and "GX" not in subtypes and "EX" not in subtypes


card = PokemonCardDef(
    guid="a2bb0107-d0be-5001-9456-e8957ab4c98f",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Ability(
            title="Queen's Call",
            game_text="Once during your turn (before your attack), you may search your deck for a Pokémon that isn't a Pokémon-GX or Pokémon-EX, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(_queens_call_target, count=1, reveal=True,
                                  prompt="Choose a Pokémon that isn't a Pokémon-GX or Pokémon-EX."),
        ),
        Attack(
            title="Power Lariat",
            game_text="This attack does 50 more damage for each Evolution Pokémon on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("mine", is_evolution_pokemon), 50, base=10),
        ),
    ],
)
