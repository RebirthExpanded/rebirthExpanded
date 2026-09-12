"""Team Rocket's Articuno (SV - Destined Rivals 51/182 -- JP M2a 034, the art here).

Basic Water Pokemon. HP 120, weakness Lightning x2, resistance Fighting
-30, retreat 1.

  Ability  Repelling Veil  Prevent all effects of attacks used by your
                           opponent's Pokemon done to your Basic Team
                           Rocket's Pokemon. (Existing effects are not
                           removed. Damage is not an effect.)
  Dark Frost [WCC] 60+  If this Pokemon has any Team Rocket's Energy
                        attached, this attack does 60 more damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, def_for
from spirit.game.session.effects import is_basic_pokemon_in_play
from spirit.game.session.passives import carrier_pokemon


def _basic_team_rockets(target, carrier):
    holder = carrier_pokemon(carrier)
    if holder is None or target.owning_player_id != holder.owning_player_id:
        return False
    name = getattr(def_for(target.archetype_id), "display_name", "") or ""
    return "Team Rocket's" in name and is_basic_pokemon_in_play(target)


def _has_team_rockets_energy(ctx) -> bool:
    return any((getattr(def_for(e.archetype_id), "display_name", "") or "") == "Team Rocket's Energy"
               for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="b8176b9d-74e1-573d-ad92-fee61b7a3f97",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsArticuno.Name",
    display_name="Team Rocket's Articuno",
    searchable_by=["Team Rocket's Articuno", "Basic", "TeamRocketsArticuno"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=144,
    abilities=[
        Ability(title="Repelling Veil",
                game_text="Prevent all effects of attacks used by your opponent's Pokémon done to your Basic Team Rocket's Pokémon. (Existing effects are not removed. Damage is not an effect.)",
                passive=attack_effect_shield_passive(protects=_basic_team_rockets)),
        Attack(title="Dark Frost",
               game_text="If this Pokémon has any Team Rocket's Energy attached, this attack does 60 more damage.",
               cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
               damage=60, damage_operator="+",
               effect=bonus_if(_has_team_rockets_energy, 60)),
    ],
)
