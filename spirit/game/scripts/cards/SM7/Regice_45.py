"""Regice (SM - Celestial Storm 45/168 -- JP SM7 031/096, the art here).

Basic Water Pokemon. HP 120, weakness Metal x2, retreat 3.

  Ability: Icy Barrier  As long as this Pokemon is your Active Pokemon,
                        your opponent can't play any Stadium cards from
                        their hand.
  Icy Wind [WCC] 60  Your opponent's Active Pokemon is now Asleep.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_stadium_card
from spirit.game.session.passives import Passive


class IcyBarrierPassive(Passive):
    def blocks_trainer_play(self, card, player_id, carrier):
        return (is_in_active_spot(carrier) and player_id != carrier.owning_player_id
                and is_stadium_card(card))


card = PokemonCardDef(
    guid="cd45e954-c1cf-5cc0-96b8-36b7bfa772d3",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Ability(
            title="Icy Barrier",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent can't play any Stadium cards from their hand.",
            passive=IcyBarrierPassive(),
        ),
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
