"""Aegislash-EX (JP XY Hyper Metal Chain Deck 60 -- HMC 005/018; English
print XY - Phantom Forces 65/119).

Basic Metal Pokemon-EX. HP 170, weakness Fire x2, resistance Psychic -20,
retreat 3.

  Ability  Mighty Shield  Prevent all damage done to this Pokemon by
                          attacks from each of your opponent's Pokemon that
                          has Special Energy attached to it.
  Slash Blast  [CCC] 40+  This attack does 20 more damage for each [M]
                          Energy attached to this Pokemon.

The shield looks at the attacking Pokemon's attachments at the moment the
damage is done; a Double Colorless Energy is enough. Slash Blast counts
Energy CARDS providing [M] (one Metal Energy = +20).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_special_energy
from spirit.game.session.passives import Passive, carrier_pokemon


class MightyShieldPassive(Passive):
    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target is not carrier_pokemon(carrier) or calc.attacker is None:
            return False
        return any(is_special_energy(e)
                   for e in calc.board.attached_energies(calc.attacker))


card = PokemonCardDef(
    guid="aff6aea8-e9a5-58be-9d45-bd118d0d2010",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AegislashEX.Name",
    display_name="Aegislash-EX",
    searchable_by=["Aegislash-EX", "Basic", "EX", "AegislashEX"],
    subtypes=["Basic", "EX"],
    collector_number=5,
    set_code="HMC",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=681,
    abilities=[
        Ability(
            title="Mighty Shield",
            game_text="Prevent all damage done to this Pokémon by attacks from each of your opponent's Pokémon that has Special Energy attached to it.",
            passive=MightyShieldPassive(),
        ),
        Attack(
            title="Slash Blast",
            game_text="This attack does 20 more damage for each [M] Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=damage_per(count_energy("self", PokemonTypes.METAL, cards=True), 20, base=40),
        ),
    ],
)
