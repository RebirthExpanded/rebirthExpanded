"""Tyranitar (SV09 95 -- JP SV9 058; English JTG/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc

from spirit.game.session.effects import is_item_card


class DauntingGazePassive(Passive):
    """While this Pokemon is in the Active Spot, the opponent can't play
    Item cards from their hand (an Ability)."""

    def blocks_trainer_play(self, card, player_id, carrier):
        return (player_id != carrier.owning_player_id and is_item_card(card)
                and pc.is_in_active_spot(carrier))
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b8a967f3-fc62-51f8-a24c-d9687714ad8a",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=95,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Daunting Gaze",
            game_text="As long as this Pokémon is in the Active Spot, your opponent can't play any Item cards from their hand.",
            passive=DauntingGazePassive(),
        ),
        Attack(
            title="Cracking Stomp",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=ac.mill_attack(2),
        ),
    ],
)
