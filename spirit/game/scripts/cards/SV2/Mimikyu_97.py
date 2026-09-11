"""Mimikyu (SV - Paldea Evolved 97/193 -- JP SV2P 034/071, the art here).

Basic Psychic Pokemon. HP 70, weakness Metal x2, no resistance, retreat 1.

  Ability  Safeguard  Prevent all damage done to this Pokemon by attacks
                      from your opponent's Pokemon ex and Pokemon V.
  Ghost Eye [PC]  Put 7 damage counters on your opponent's Active Pokemon.

Safeguard is Sylveon SV085's shape widened to Pokemon V (V, VSTAR, VMAX,
V-UNION). Damage only: effects of those attacks still land. Ghost Eye
places counters (no Weakness, no attack-damage shields).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    is_pokemon_ex, is_pokemon_v)
from spirit.game.session.passives import carrier_pokemon


def _safeguard(calc, carrier):
    if carrier_pokemon(carrier) is not calc.target or calc.attacker is None:
        return False
    archetype = calc.attacker.archetype_id
    return is_pokemon_ex(archetype) or is_pokemon_v(archetype)


async def ghost_eye(ctx):
    """7 damage counters on the opponent's Active."""
    defender = ctx.opponent_active()
    if defender is None:
        return
    await ctx.deal_damage(70, target=defender, apply_modifiers=False,
                          as_counters=True)


card = PokemonCardDef(
    guid="a393dec6-f9f8-5bf5-b1e1-bc14160b4e94",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=778,
    abilities=[
        Ability(title="Safeguard",
                game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex and Pokémon V.",
                passive=prevent_damage_when(_safeguard)),
        Attack(title="Ghost Eye",
               game_text="Put 7 damage counters on your opponent's Active Pokémon.",
               cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
               effect=ghost_eye),
    ],
)
