"""Ampharos (ME4 29 -- JP M4 029; English CRI/29, CRI/90, MEP/75). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class SynchroPulsePassive(Passive):
    """Same hand size as the opponent: this Pokemon's attacks do +80 to the
    opponent's Active (before Weakness and Resistance). An Ability."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active and calc.attacker is carrier):
            return
        board = calc.board
        mine = board.find_player_area(carrier.owning_player_id, "hand")
        other = next((pid for pid in board.player_ids if pid != carrier.owning_player_id), None)
        theirs = board.find_player_area(other, "hand") if other else None
        if mine is not None and theirs is not None and len(mine.children) == len(theirs.children):
            calc.amount += 80


card = PokemonCardDef(
    guid="5acc2c28-f0c1-51c8-91cd-232645da1d75",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Synchro Pulse",
            game_text="If you have the same number of cards in your hand as your opponent, attacks used by this Pokémon do 80 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=SynchroPulsePassive(),
        ),
        Attack(
            title="Flashing Bolt",
            game_text="During your next turn, this Pokémon can't use Flashing Bolt.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
            locks_next_turn=True,
        ),
    ],
)
