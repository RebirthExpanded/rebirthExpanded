"""Pyroar (ME1 24 -- JP M1S 011; English MEG/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class IntimidatingFangPassive(Passive):
    """While this Pokemon is Active, the opponent's Active Pokemon's attacks
    do 30 less damage (before W/R) (an Ability)."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        attacker = calc.attacker
        if (calc.is_attack and attacker is not None and pc.is_in_active_spot(me)
                and attacker.owning_player_id != me.owning_player_id and pc.is_in_active_spot(attacker)):
            calc.amount = max(0, calc.amount - 30)


card = PokemonCardDef(
    guid="d2ea4669-58fd-5712-9f3b-d24f14fde9fe",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    display_name="Pyroar",
    searchable_by=["Pyroar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 30 less damage (before applying Weakness and Resistance).",
            passive=IntimidatingFangPassive(),
        ),
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
