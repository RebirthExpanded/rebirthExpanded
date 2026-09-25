"""Garchomp (SM - Unified Minds 114/236 -- JP SM10a 036/054).

Stage 2 Fighting Pokemon, evolves from Gabite. HP 150, weakness Grass x2,
no retreat cost.

  Ability  Avenging Aura  If you have more Prize cards remaining than your
                          opponent, this Pokemon's attacks do 80 more damage
                          to your opponent's Active Pokemon (before applying
                          Weakness and Resistance).
  Over Slice  [FC] 80+  You may discard an Energy from this Pokemon. If you
                        do, this attack does 40 more damage.

The Prize comparison is Karate Belt's (support_common).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import discard_for_bonus
from spirit.game.card_effects.support_common import more_prizes_remaining_than_opponent
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


class AvengingAuraPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if attacker is None or carrier_pokemon(carrier) is not attacker:
            return
        if more_prizes_remaining_than_opponent(calc.board, attacker.owning_player_id):
            calc.amount += 80


card = PokemonCardDef(
    guid="ce404e4d-bd5e-5016-8a8d-744a8cfce71f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=['Garchomp', 'Stage 2', 'Garchomp'],
    subtypes=['Stage 2'],
    collector_number=114,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Avenging Aura",
            game_text="If you have more Prize cards remaining than your opponent, this Pokémon's attacks do 80 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=AvengingAuraPassive(),
        ),
        Attack(title="Over Slice", game_text="You may discard an Energy from this Pokémon. If you do, this attack does 40 more damage.",
               cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=80, damage_operator="+",
               effect=discard_for_bonus(source="self-energy", max_count=1, flat=40, prompt="You may discard an Energy from this Pokémon")),
    ],
)
