"""Pikachu (ME6A 22 -- JP M6a 022; English 30C/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class LonelyGazePassive(Passive):
    """While this Pokemon is Active, the opponent's Active Pokemon's attacks
    do 20 less damage (before Weakness and Resistance)."""

    def modify_damage_dealt(self, calc, carrier):
        a = calc.attacker
        if not (calc.is_attack and a is not None and a.owning_player_id != carrier.owning_player_id):
            return
        if pc.is_in_active_spot(carrier) and calc.board.active_pokemon(a.owning_player_id) is a:
            calc.amount = max(0, calc.amount - 20)


card = PokemonCardDef(
    guid="39473837-e1d8-5ee1-82a0-85bfc15bde66",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Ability(
            title="Lonely Gaze",
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 20 less damage (before applying Weakness and Resistance).",
            passive=LonelyGazePassive(),
        ),
        Attack(
            title="Pika Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
