"""Mewtwo V-UNION -- the combined Pokemon (SWSH Promos 159-162 -- JP
Special Card Set 005-008/013, the art here is the four pieces together).

Psychic Pokemon V-UNION. HP 310, weakness Darkness x2, resistance
Fighting -30, retreat 2. When Knocked Out, the opponent takes 3 Prizes.

  Union Gain          [C]        Attach up to 2 [P] Energy cards from your
                                 discard pile to this Pokemon.
  Super Regeneration  [PC]       Heal 200 damage from this Pokemon.
  Psysplosion         [PC]       Put 16 damage counters on your opponent's
                                 Pokemon in any way you like.
  Photon Barrier      (Ability)  Prevent all effects of attacks from your
                                 opponent's Pokemon done to this Pokemon.
                                 (Damage is not an effect.)
  Final Burn          [PPC] 300

Runtime-only: the four pieces (MewtwoVUNION_159..162) name it and the
assembly rule on each builds it from the discard pile (session/legends.py).
Number 902 is this pool's own for the combined face.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.card_effects.pokemon import union_gain_attack
from spirit.game.data_utils import Ability, Attack, VUnionPokemonDef

NAME = "com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVUNION.Name"


async def super_regeneration(ctx):
    await ctx.heal(200, ctx.attacker)


UNION_GAIN = union_gain_attack(PokemonTypes.PSYCHIC)
SUPER_REGENERATION = Attack(
    title="Super Regeneration",
    game_text="Heal 200 damage from this Pokémon.",
    cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
    effect=super_regeneration,
)
PSYSPLOSION = Attack(
    title="Psysplosion",
    game_text="Put 16 damage counters on your opponent's Pokémon in any way you like.",
    cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
    effect=place_counters(16, target="choose_any_opponent"),
)
PHOTON_BARRIER = Ability(
    title="Photon Barrier",
    game_text="Prevent all effects of attacks from your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
    passive=attack_effect_shield_passive(),
)
FINAL_BURN = Attack(
    title="Final Burn",
    game_text="",
    cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
    damage=300,
)


card = VUnionPokemonDef(
    guid="bf50a130-5ce2-5299-966b-dbd6c7b9f6e1",
    key="Promo_SWSH",
    name=NAME,
    display_name="Mewtwo V-UNION",
    searchable_by=["Mewtwo V-UNION", "V-UNION", "MewtwoVUNION"],
    subtypes=["V-UNION"],
    collector_number=902,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareUltra,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[UNION_GAIN, SUPER_REGENERATION, PSYSPLOSION, PHOTON_BARRIER, FINAL_BURN],
)
