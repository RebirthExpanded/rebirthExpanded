"""Entei (SV3 30 -- JP SV3 016; English OBF/30, PAF/112). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class _ActiveDebuff(Passive):
    """While this Pokemon is Active, the opponent's Active Pokemon's attacks
    do N less damage (before W/R)."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        attacker = calc.attacker
        if (calc.is_attack and attacker is not None and pc.is_in_active_spot(me)
                and attacker.owning_player_id != me.owning_player_id and pc.is_in_active_spot(attacker)):
            calc.amount = max(0, calc.amount - self.amount)
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="bd895685-2028-5900-967b-9f3c735daec4",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Pressure",
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 20 less damage (before applying Weakness and Resistance).",
            passive=_ActiveDebuff(20),
        ),
        Attack(
            title="Blaze Ball",
            game_text="This attack does 20 more damage for each Fire Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.FIRE), 20, base=60),
        ),
    ],
)
