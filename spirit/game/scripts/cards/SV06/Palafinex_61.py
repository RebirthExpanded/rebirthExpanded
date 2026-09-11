"""Palafin ex (SV - Twilight Masquerade 61/167 -- JP SV6 036/101).

Stage 1 Water Pokemon ex, evolves from Finizen. HP 340, weakness
Lightning x2, retreat 2.

  Ability  Hero's Spirit  Put this Pokemon into play only with the effect
                          of Palafin's Zero to Hero Ability.
  Giga Impact  [W] 250  During your next turn, this Pokemon can't attack.

Hero's Spirit is an Ability, so an Ability lock that reaches the hand
(Garbotoxin) switches it off and this card can then be evolved onto a
Finizen from the hand like any Stage 1: unplayable_from_hand is a
predicate reading abilities_disabled for the card in hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import abilities_disabled


def _heros_spirit_binds(board, player_id, card) -> bool:
    return not abilities_disabled(board, card)


card = PokemonCardDef(
    guid="13336204-b982-539c-9dc3-9db4a236e48f",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafinex.Name",
    display_name="Palafin ex",
    searchable_by=["Palafin ex", "Stage 1", "ex", "Palafinex"],
    subtypes=["Stage 1", "ex"],
    collector_number=61,
    set_code="SV06",
    rarity=Rarities.RareUltra,
    hp=340,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    regulation_mark="H",
    unplayable_from_hand=_heros_spirit_binds,
    abilities=[
        Ability(
            title="Hero's Spirit",
            game_text="Put this Pokémon into play only with the effect of Palafin's Zero to Hero Ability.",
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1},
            damage=250,
            locks_next_turn=True,
        ),
    ],
)
