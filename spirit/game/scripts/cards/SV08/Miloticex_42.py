"""Milotic ex (SV - Surging Sparks 42/191 -- JP SV8 026/106, the art here).

Stage 1 Water Pokemon ex, evolves from Feebas. HP 270, weakness Lightning
x2, no resistance, retreat 2.

  Ability  Sparkling Scales  Prevent all damage from and effects of attacks
                             from your opponent's Tera Pokemon done to this
                             Pokemon.
  Hypno Splash [WCC] 160  Your opponent's Active Pokemon is now Asleep.

Sparkling Scales reads the attacker's Tera subtype: damage through
prevents_damage, effects through blocks_attack_effects (source = the
attacking Pokemon).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_tera(pokemon) -> bool:
    return pokemon is not None and "Tera" in subtypes_for(pokemon.archetype_id)


class SparklingScalesPassive(Passive):
    def prevents_damage(self, calc, carrier):
        return (calc.is_attack and calc.is_opposing
                and carrier_pokemon(carrier) is calc.target
                and _is_tera(calc.attacker))

    def blocks_attack_effects(self, target, carrier, source=None):
        if carrier_pokemon(carrier) is not target or source is None:
            return False
        return source.owning_player_id != target.owning_player_id and _is_tera(source)


card = PokemonCardDef(
    guid="0823cc2b-f2ef-5f20-b69e-e81261962144",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miloticex.Name",
    display_name="Milotic ex",
    searchable_by=["Milotic ex", "Stage 1", "ex", "Miloticex"],
    subtypes=["Stage 1", "ex"],
    collector_number=42,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(title="Sparkling Scales",
                game_text="Prevent all damage from and effects of attacks from your opponent's Tera Pokémon done to this Pokémon.",
                passive=SparklingScalesPassive()),
        Attack(title="Hypno Splash",
               game_text="Your opponent's Active Pokémon is now Asleep.",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
               damage=160, effect=condition_attack(SpecialConditions.ASLEEP)),
    ],
)
