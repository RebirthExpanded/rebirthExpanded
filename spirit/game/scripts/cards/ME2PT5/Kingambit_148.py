"""Kingambit (ME2PT5 148 -- JP M2a 118; English ASC/148). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac



class SupremeOverlordPassive(Passive):
    """+30 to the opponent's Active for each Prize card the opponent has
    taken (before W/R) (an Ability)."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.attacker is me and calc.to_active and calc.is_opposing):
            return
        taken = calc.board.prizes_taken(calc.target.owning_player_id)
        calc.amount += 30 * taken


card = PokemonCardDef(
    guid="997602f1-f77e-5005-9be0-d11495bf974f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingambit.Name",
    display_name="Kingambit",
    searchable_by=["Kingambit", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=148,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    family_id=624,
    abilities=[
        Ability(
            title="Supreme Overlord",
            game_text="Attacks used by this Pokémon do 30 more damage to your opponent's Active Pokémon for each Prize card your opponent has taken (before applying Weakness and Resistance).",
            passive=SupremeOverlordPassive(),
        ),
        Attack(
            title="Double-Edged Slash",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.METAL: 2},
            damage=180,
            effect=ac.recoil_attack(50),
        ),
    ],
)
