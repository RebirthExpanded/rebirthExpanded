"""Farigiraf ex (SV - Temporal Forces 108/162 -- JP SV5M 042/071, the art here).

Stage 1 Darkness Tera Pokemon ex, evolves from Girafarig. HP 260, weakness
Grass x2, no resistance, retreat 2.

  Tera  As long as this Pokemon is on your Bench, prevent all damage done
        to it by attacks (yours and your opponent's).
  Ability  Armor Tail  Prevent all damage done to this Pokemon by attacks
                       from your opponent's Basic Pokemon ex.
  Dirty Beam [PCC] 160  This attack also does 30 damage to 1 of your
                        opponent's Benched Pokemon. (Don't apply Weakness
                        and Resistance for Benched Pokemon.)

Armor Tail is damage only (effects still land) and reads the attacker as
it sits in play: a Basic Pokemon ex, either era's ex/EX.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, is_pokemon_ex
from spirit.game.session.effects import is_basic_pokemon_in_play
from spirit.game.session.passives import carrier_pokemon


def _armor_tail(calc, carrier):
    if carrier_pokemon(carrier) is not calc.target or calc.attacker is None:
        return False
    return is_pokemon_ex(calc.attacker.archetype_id) and is_basic_pokemon_in_play(calc.attacker)


card = PokemonCardDef(
    guid="10744bb2-a8f3-590e-9096-2829d61fc8c8",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farigirafex.Name",
    display_name="Farigiraf ex",
    searchable_by=["Farigiraf ex", "Stage 1", "ex", "Tera", "Farigirafex"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=108,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    family_id=203,
    passive=TeraRulePassive(),
    abilities=[
        Ability(title="Armor Tail",
                game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Basic Pokémon ex.",
                passive=prevent_damage_when(_armor_tail)),
        Attack(title="Dirty Beam",
               game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
               cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
               damage=160, effect=snipe_attack(30, also_base=True)),
    ],
)
