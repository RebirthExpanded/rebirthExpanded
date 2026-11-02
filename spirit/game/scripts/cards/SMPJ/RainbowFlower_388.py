"""Rainbow Flower (SMPJ 388 -- JP SMP 388; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.card_effects.passives_common import HpBonusPassive, is_in_active_spot
from spirit.game.card_effects.smp import is_gx_pokemon
from spirit.game.session.passives import carrier_pokemon


class RainbowFlowerPassive(HpBonusPassive):
    """The Pokemon-GX holding it gets +20 HP and, while Benched, takes no
    damage from the opponent's attacks."""

    def __init__(self):
        super().__init__(20, holder_pred=is_gx_pokemon)

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        return (calc.is_attack and calc.is_opposing and holder is not None
                and calc.target is holder and is_gx_pokemon(holder)
                and not is_in_active_spot(holder))


card = PokemonToolCardDef(
    guid="6478715b-3892-5944-ad85-a7fab32b97e5",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RainbowFlower.Name",
    display_name="Rainbow Flower",
    searchable_by=["Rainbow Flower", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=388,
    set_code="SMPJ",
    regulation_mark="C",
    rarity=Rarities.RarePromo,
    passive=RainbowFlowerPassive(),
)
