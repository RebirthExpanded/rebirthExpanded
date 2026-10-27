"""Annihilape (SV10 92 -- JP SV10 047; English DRI/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10



class LoseCoolPassive(Passive):
    """2+ damage counters: this Pokemon's attacks do 120 more to the
    opponent's Active (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if (calc.is_attack and calc.attacker is me and calc.to_active and calc.is_opposing
                and _counters(calc.board, me) >= 2):
            calc.amount += 120


card = PokemonCardDef(
    guid="dbf7bb00-a206-5b82-9383-7b36a5580205",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilape.Name",
    display_name="Annihilape",
    searchable_by=["Annihilape", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=92,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=56,
    abilities=[
        Ability(
            title="Lose Cool",
            game_text="If this Pokémon has 2 or more damage counters on it, attacks used by this Pokémon do 120 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=LoseCoolPassive(),
        ),
        Attack(
            title="Impact Blow",
            game_text="During your next turn, this Pokémon can't use Impact Blow.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=160,
            locks_next_turn=True,
        ),
    ],
)
