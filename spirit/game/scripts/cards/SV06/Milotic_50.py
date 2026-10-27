"""Milotic (SV06 50 -- JP SV6 030; English TWM/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class MentallyCalmPassive(Passive):
    """The opponent's Pokemon in play and their attached cards can't be put
    into the opponent's hand (an Ability)."""

    def blocks_put_in_hand(self, card, carrier):
        return card.owning_player_id is not None and card.owning_player_id != carrier.owning_player_id


card = PokemonCardDef(
    guid="3696d14a-43fc-50f3-976b-fb20f7239492",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Mentally Calm",
            game_text="Your opponent's Pokémon in play and all attached cards can't be put into your opponent's hand.",
            passive=MentallyCalmPassive(),
        ),
        Attack(
            title="Hydro Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
