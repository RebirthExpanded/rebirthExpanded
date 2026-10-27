"""Noivern (SV09 128 -- JP SV9 081; English JTG/128). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon



class TuningEchoPassive(Passive):
    """Same hand size as the opponent: Frightening Howl (this Pokemon's only
    attack) costs no Energy (an Ability)."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        mine = board.find_player_area(carrier.owning_player_id, "hand")
        other = next((pid for pid in board.player_ids if pid != carrier.owning_player_id), None)
        theirs = board.find_player_area(other, "hand") if other else None
        if mine is not None and theirs is not None and len(mine.children) == len(theirs.children):
            return {}
        return cost


card = PokemonCardDef(
    guid="b8d82aad-2f0b-580a-b1af-b04eadac88ac",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name",
    display_name="Noivern",
    searchable_by=["Noivern", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=128,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Ability(
            title="Tuning Echo",
            game_text="If you have the same number of cards in your hand as your opponent, ignore all Energy in the cost of Frightening Howl used by this Pokémon.",
            passive=TuningEchoPassive(),
        ),
        Attack(
            title="Frightening Howl",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
