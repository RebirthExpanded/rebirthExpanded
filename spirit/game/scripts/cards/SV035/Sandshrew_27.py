"""Sandshrew (SV035 27 -- JP SV2a 027; English MEW/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class SandScreenPassive(Passive):
    """The opponent's Items/Supporters can't put Trainer cards from their
    discard pile into their deck (an Ability)."""

    def blocks_trainer_recycle(self, card, player_id, carrier):
        return player_id != carrier.owning_player_id and card.owning_player_id == player_id


card = PokemonCardDef(
    guid="78c0e37e-11f4-5b64-a90f-44ffbac6aa5d",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    display_name="Sandshrew",
    searchable_by=["Sandshrew", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=27,
    abilities=[
        Ability(
            title="Sand Screen",
            game_text="Trainer cards in your opponent's discard pile can't be put into their deck by an effect of your opponent's Item or Supporter cards.",
            passive=SandScreenPassive(),
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
