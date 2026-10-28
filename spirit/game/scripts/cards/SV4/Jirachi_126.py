"""Jirachi (SV4 126 -- JP SV3a 042; English PAR/126). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.trainers import is_basic_energy_card

from spirit.game.session.effects import is_basic_pokemon_in_play


class StellarVeilPassive(Passive):
    """Your Benched Pokemon: no damage counters from effects of attacks used
    by the opponent's Basic Pokemon (an Ability). Damage is not a counter."""

    def blocks_attack_counters(self, target, attacker, carrier):
        return (target.owning_player_id == carrier.owning_player_id
                and target._containing_area_name() == "bench"
                and attacker.owning_player_id != carrier.owning_player_id
                and is_basic_pokemon_in_play(attacker))


card = PokemonCardDef(
    guid="1eec8e0d-9212-57e6-9a9e-128ebbb790bb",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=385,
    abilities=[
        Ability(
            title="Stellar Veil",
            game_text="Prevent all damage counters from being placed on your Benched Pokémon by effects of attacks used by your opponent's Basic Pokémon.",
            passive=StellarVeilPassive(),
        ),
        Attack(
            title="Charge Energy",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_basic_energy_card, count=2, reveal=True, prompt="Choose up to 2 Basic Energy cards."),
        ),
    ],
)
