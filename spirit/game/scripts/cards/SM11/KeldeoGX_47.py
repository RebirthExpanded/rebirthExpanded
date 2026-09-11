"""Keldeo-GX (SM - Unified Minds 47/236 -- JP SM10b 019/054).

Basic Water Pokemon-GX. HP 170, weakness Grass x2, retreat 2.

  Ability  Pure Heart  Prevent all effects of attacks, including damage,
                       done to this Pokemon by your opponent's Pokemon-GX
                       or Pokemon-EX.
  Sonic Edge  [WWC] 110  This attack's damage isn't affected by any
                         effects on your opponent's Active Pokemon.
  Resolute Blade-GX  [WWC] 50x  This attack does 50 damage for each of
                                your opponent's Benched Pokemon.

Pure Heart is both a damage and an attack-effect shield keyed on the
attacker's rule box; the effect shield is also what lets Keldeo-GX use
Resolute Blade-GX under Latios-GX's Clear Vision-GX. Pokemon-EX is the
uppercase box; a Scarlet & Violet ex is not shielded against.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import (count_bench, damage_per,
                                                     ignore_effects_attack)
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_gx_or_ex(pokemon) -> bool:
    if pokemon is None:
        return False
    subs = subtypes_for(pokemon.archetype_id)
    return "GX" in subs or "EX" in subs


class PureHeartPassive(Passive):
    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target is not carrier_pokemon(carrier):
            return False
        return _is_gx_or_ex(calc.attacker)

    def blocks_attack_effects(self, target, carrier, source=None):
        holder = carrier_pokemon(carrier)
        if holder is None or target is not holder or source is None:
            return False
        if source.owning_player_id == holder.owning_player_id:
            return False
        return _is_gx_or_ex(source)


card = PokemonCardDef(
    guid="664238cf-bb63-5dea-9fdc-801db8a8c0ba",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KeldeoGX.Name",
    display_name="Keldeo-GX",
    searchable_by=["Keldeo-GX", "Basic", "GX", "KeldeoGX"],
    subtypes=["Basic", "GX"],
    collector_number=47,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Ability(
            title="Pure Heart",
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon-GX or Pokémon-EX.",
            passive=PureHeartPassive(),
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=ignore_effects_attack(),
        ),
        Attack(
            title="Resolute Blade-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            gx=True,
            effect=damage_per(count_bench("opponent"), 50),
        ),
    ],
)
