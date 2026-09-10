"""Beast Energy {*} (SM - Forbidden Light 117/131).

Special Energy, Prism Star.

  "This card provides [C] Energy. While this card is attached to an Ultra
   Beast, it provides every type of Energy but provides only 1 Energy at a
   time. The attacks of the Ultra Beast this card is attached to do 30 more
   damage to your opponent's Active Pokemon (before applying Weakness and
   Resistance)."

Two effects off the same question -- is the holder an Ultra Beast -- so
one passive carries both: Aurora Energy's rainbow for the cost side, and a
+30 that fires only when the holder itself is the attacker and only against
the opponent's Active, before Weakness and Resistance.

Ultra Beast is the subtype Naganadel-GX and Naganadel & Guzzlord-GX already
carry, so nothing new is needed to recognise one.

The Prism Star rule -- one per deck by name, and the Lost Zone instead of
the discard pile -- rides the "Prism Star" subtype, which data_utils
already reads for both.
"""

from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_ultra_beast(pokemon) -> bool:
    return "Ultra Beast" in subtypes_for(pokemon.archetype_id)


class BeastEnergyPassive(Passive):
    """On an Ultra Beast: every type of Energy, and +30 on its attacks."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or carrier_pokemon(energy) is not holder:
            return options
        if not _is_ultra_beast(holder):
            return options
        return [[t.value] for [t] in ALL_TYPES_ONE_AT_A_TIME]

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not _is_ultra_beast(holder):
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.attacker is not holder:
            return
        calc.amount += 30


card = EnergyCardDef(
    guid="c2beaa3f-8758-59db-9154-a5293a4c25e4",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.energy.BeastEnergyPrismStar.Name",
    display_name="Beast Energy {*}",
    searchable_by=["Beast Energy", "Special", "Prism Star", "BeastEnergy"],
    subtypes=["Special", "Prism Star"],
    collector_number=117,
    set_code="SM6",
    rarity=Rarities.Prism,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=BeastEnergyPassive(),
)
