"""Magmortar (SV09 21 -- JP SV9 014; English JTG/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon



class MagmaSurgePassive(Passive):
    """Pokemon Checkup puts 3 more damage counters on the opponent's Burned
    Pokemon (an Ability)."""

    def modify_burn_counters(self, counters, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return counters + 3
        return counters


card = PokemonCardDef(
    guid="24dbb9e6-75de-512a-968d-763bbebc82b4",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    family_id=240,
    abilities=[
        Ability(
            title="Magma Surge",
            game_text="During Pokémon Checkup, put 3 more damage counters on your opponent's Burned Pokémon.",
            passive=MagmaSurgePassive(),
        ),
        Attack(
            title="Searing Flame",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=ac.condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)
