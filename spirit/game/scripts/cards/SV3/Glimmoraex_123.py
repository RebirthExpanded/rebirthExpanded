"""Glimmora ex (SV3 123 -- JP SV3 065; English OBF/123, OBF/213, PAF/218). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class DustFieldPassive(Passive):
    """Active: the opponent can't have more than 3 Benched Pokemon."""

    def bench_capacity(self, player_id, carrier):
        if player_id != carrier.owning_player_id and pc.is_in_active_spot(carrier):
            return 3
        return None


card = PokemonCardDef(
    guid="cd58d8f5-0b6e-5574-9170-1b9f107c422f",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmoraex.Name",
    display_name="Glimmora ex",
    searchable_by=["Glimmora ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=123,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    family_id=969,
    abilities=[
        Ability(
            title="Dust Field",
            game_text="As long as this Pokémon is in the Active Spot, your opponent can't have more than 3 Benched Pokémon. If they have 4 or more Benched Pokémon, they discard Benched Pokémon until they have 3 Pokémon on the Bench. If more than one effect changes the number of Benched Pokémon allowed, use the smaller number.",
            passive=DustFieldPassive(),
        ),
        Attack(
            title="Poisonous Gem",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=140,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
