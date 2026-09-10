"""Mew (SM - Unbroken Bonds 76/214 -- JP SM10 037/095).

Basic Psychic. HP 60, weakness Psychic x2, retreat 1.

  Ability  Bench Barrier  Prevent all damage done to your Benched Pokemon
                          by your opponent's attacks.

  Psypower  [C]  Put 3 damage counters on your opponent's Pokemon in any
                 way you like.

Mr. Mime's Bench Barrier, narrowed to the opponent's attacks -- the BW-era
Mr. Mime says "by attacks" and shields the Bench from the owner's own
spread too, this one does not. That is the difference between the two
printings and the reason it does not simply reuse Mr. Mime's passive.

Psypower places counters rather than dealing damage, so Weakness and
Resistance never enter into it and a Benched target is as reachable as the
Active one.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive, carrier_pokemon

COUNTERS = 3


class BenchBarrierPassive(Passive):
    """The carrier's Benched allies take no damage from opposing attacks."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not (calc.is_attack and calc.is_opposing):
            return False
        target = calc.target
        if target is None or target.owning_player_id != holder.owning_player_id:
            return False
        return target._containing_area_name() == "bench"


card = PokemonCardDef(
    guid="418199c6-0aec-556a-9c9d-669b000af72a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pokémon by your opponent's attacks.",
            passive=BenchBarrierPassive(),
        ),
        Attack(
            title="Psypower",
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=place_counters(COUNTERS, target="choose_any_opponent"),
        ),
    ],
)
