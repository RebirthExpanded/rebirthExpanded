"""Rhyperior (SV07 76 -- JP SV7 052; English SCR/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import TrainerType


class WideWallPassive(Passive):
    """Active: the opponent's Supporters do nothing to your Pokemon."""

    def blocks_trainer_effects(self, affected_player_id, trainer_card, trainer_type, carrier,
                               affected_entity=None, board=None):
        return (pc.is_in_active_spot(carrier) and trainer_type == TrainerType.SUPPORTER.value
                and trainer_card is not None and trainer_card.owning_player_id != carrier.owning_player_id
                and affected_entity is not None and getattr(affected_entity, "owning_player_id", None) == carrier.owning_player_id
                and carrier_pokemon(affected_entity) is not None)


card = PokemonCardDef(
    guid="1bd08e12-d56c-52a0-8bda-5abb9e2657f7",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Ability(
            title="Wide Wall",
            game_text="As long as this Pokémon is in the Active Spot, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to all of your Pokémon.",
            passive=WideWallPassive(),
        ),
        Attack(
            title="Drill Run",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=ac.discard_opponent_energy_attack(1),
        ),
    ],
)
