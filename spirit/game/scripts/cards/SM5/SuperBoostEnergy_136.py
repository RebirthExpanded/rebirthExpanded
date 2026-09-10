"""Super Boost Energy {*} (SM - Ultra Prism 136/156 -- JP SM5M 065/066).

Special Energy, Prism Star.

  "This card provides [C] Energy. While this card is attached to a Stage 2
   Pokemon, it provides every type of Energy but provides only 1 Energy at
   a time, and if you have 3 or more Stage 2 Pokemon in play, it provides
   every type of Energy and provides 4 Energy at a time."

Two switches on the same card, and the second one only opens while the
first is open: a Stage 2 holder makes it a rainbow, a board with three of
them makes that rainbow worth four. On anything else it is the printed
single Colorless, so a Stage 1 or a Basic gets nothing out of it at all.

max_energy_provided = 4 is the pip's ceiling: the pip names the card, not
what it happens to be worth this turn, so a card that can act as four
Energy is drawn with the emblems its art prints.

The Prism Star rule -- one per deck by name, Lost Zone instead of the
discard -- rides the subtype, as it does for Beast Energy.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.passives import Passive, carrier_pokemon

STAGE2_FOR_FOUR = 3
ALL_TYPES_FOUR_AT_A_TIME = [[option[0].value] * 4
                            for option in ALL_TYPES_ONE_AT_A_TIME]


def _is_stage_2(pokemon) -> bool:
    return pokemon.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value


class SuperBoostEnergyPassive(Passive):
    """Rainbow on a Stage 2; four at a time once three Stage 2 are in play."""

    max_energy_provided = 4   # the pip has to show what the card can be

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or carrier_pokemon(energy) is not holder:
            return options
        if not _is_stage_2(holder):
            return options
        owner = energy.owning_player_id or holder.owning_player_id
        stage_2s = sum(1 for p in board.pokemon_in_play(owner) if _is_stage_2(p)) \
            if owner else 0
        if stage_2s >= STAGE2_FOR_FOUR:
            return [list(option) for option in ALL_TYPES_FOUR_AT_A_TIME]
        return [[t.value] for [t] in ALL_TYPES_ONE_AT_A_TIME]


card = EnergyCardDef(
    guid="a40d9de4-8a50-599e-acbb-b4019632a73d",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.energy.SuperBoostEnergyPrismStar.Name",
    display_name="Super Boost Energy {*}",
    searchable_by=["Super Boost Energy", "Special", "Prism Star",
                   "SuperBoostEnergy"],
    subtypes=["Special", "Prism Star"],
    collector_number=136,
    set_code="SM5",
    rarity=Rarities.Prism,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=SuperBoostEnergyPassive(),
)
