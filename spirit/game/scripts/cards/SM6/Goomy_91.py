"""Goomy (SM - Forbidden Light 91/131 -- JP SM6 065/094, the art here).

Basic Dragon Pokemon. HP 40, weakness Fairy x2, no resistance, retreat 1.

  Sticky Membrane  (Ability)  As long as this Pokemon is your Active
                              Pokemon, your opponent's Pokemon's attacks
                              cost [C] more.
  Ram              [Y]  10

The tax is the same passive Vikavolt-family cards use, gated on the
carrier standing in the Active Spot.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import OpponentAttackTaxPassive, is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef


class StickyMembranePassive(OpponentAttackTaxPassive):
    """Opposing attacks cost [C] more while Goomy is Active."""

    def __init__(self):
        super().__init__(1)

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if not is_in_active_spot(carrier):
            return cost
        return super().modify_attack_cost(cost, pokemon, carrier, board)


card = PokemonCardDef(
    guid="78677a99-4bd6-5c42-ae08-f1a27624628c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    display_name="Goomy",
    searchable_by=["Goomy", "Basic"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=704,
    abilities=[
        Ability(
            title="Sticky Membrane",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Pokémon's attacks cost [C] more.",
            passive=StickyMembranePassive(),
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
    ],
)
