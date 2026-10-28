"""Thundurus (SV3 70 -- JP SV3 036; English OBF/70, PAF/139). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac



class AdverseWeatherPassive(Passive):
    """Active: no damage to your Benched Pokemon from opposing attacks."""

    def prevents_damage(self, calc, carrier):
        me = carrier_pokemon(carrier)
        return (calc.is_attack and calc.is_opposing and pc.is_in_active_spot(me)
                and calc.target.owning_player_id == me.owning_player_id
                and calc.target._containing_area_name() == "bench")


card = PokemonCardDef(
    guid="6f4ddec5-e5a2-597a-b1ef-33995d966065",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Ability(
            title="Adverse Weather",
            game_text="As long as this Pokémon is in the Active Spot, prevent all damage done to your Benched Pokémon by attacks from your opponent's Pokémon.",
            passive=AdverseWeatherPassive(),
        ),
        Attack(
            title="Gigantic Bolt",
            game_text="This Pokémon also does 90 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=140,
            effect=ac.recoil_attack(90),
        ),
    ],
)
