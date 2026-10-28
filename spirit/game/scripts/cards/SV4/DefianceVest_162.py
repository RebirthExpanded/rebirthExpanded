"""Defiance Vest (SV4 162 -- JP SV4K 062; English PAR/162). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.session.passives import carrier_pokemon


class DefianceVestPassive(Passive):
    """More Prize cards remaining than the opponent: holder takes 40 less."""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.target is holder):
            return
        board = calc.board
        mine = board.find_player_area(holder.owning_player_id, "prizePile")
        other = next((pid for pid in board.player_ids if pid != holder.owning_player_id), None)
        theirs = board.find_player_area(other, "prizePile") if other else None
        if mine is not None and theirs is not None and len(mine.children) > len(theirs.children):
            calc.amount = max(0, calc.amount - 40)


card = PokemonToolCardDef(
    guid="25d12914-5a6e-5bbb-93b0-9e73d99652e9",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DefianceVest.Name",
    display_name="Defiance Vest",
    searchable_by=["Defiance Vest", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=162,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    passive=DefianceVestPassive(),
)
