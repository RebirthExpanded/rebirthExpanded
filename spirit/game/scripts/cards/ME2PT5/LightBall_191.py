"""Light Ball (ME2PT5 191 -- JP M2a 163; English ASC/191). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import PokemonToolCardDef

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for



class LightBallPassive(Passive):
    """The Pikachu ex it's attached to does +50 to the opponent's Active
    Pokemon ex (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.attacker is holder and calc.to_active and calc.is_opposing):
            return
        if getattr(def_for(holder.archetype_id), "display_name", "") != "Pikachu ex":
            return
        if "ex" in (subtypes_for(calc.target.archetype_id) or []):
            calc.amount += 50


card = PokemonToolCardDef(
    guid="3f0c16a3-aafa-5129-abc0-10bdc2b4bdd6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LightBall.Name",
    display_name="Light Ball",
    searchable_by=["Light Ball", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=191,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=LightBallPassive(),
)
