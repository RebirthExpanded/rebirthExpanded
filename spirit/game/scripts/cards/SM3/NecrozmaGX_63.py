"""Necrozma-GX (SM - Burning Shadows 63/147 -- JP SM3N 026/051).

Basic Psychic Pokemon-GX. HP 180, weakness Psychic x2, retreat 2.

  Ability  Light's End  Prevent all damage done to this Pokemon by attacks
                        from your opponent's [C] Pokemon.
  Prism Burst  [CCC] 10+  Discard all [P] Energy from this Pokemon. This
                          attack does 60 more damage for each card you
                          discarded in this way.
  Black Ray-GX  [CCC]  This attack does 100 damage to each of your
                       opponent's Pokemon-GX and Pokemon-EX. This damage
                       isn't affected by Weakness or Resistance.

Light's End reads the attacker's live types (a Colorless attacker made
another type by an effect is no longer [C]). Prism Burst counts CARDS
that provide [P] -- a Double Colorless is not one. Black Ray hits every
GX / uppercase-EX over there, Bench included, as attack damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.session.effects import live_pokemon_types
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.pokemon import energy_provides_type


class LightsEndPassive(Passive):
    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target is not carrier_pokemon(carrier) or calc.attacker is None:
            return False
        return PokemonTypes.COLORLESS.value in live_pokemon_types(calc.attacker)


async def prism_burst(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 99,
        predicate=lambda c: energy_provides_type(c, PokemonTypes.PSYCHIC.value),
        prompt="Discard all [P] Energy from this Pokémon")
    await ctx.deal_damage(10 + 60 * len(discarded))


def _is_gx_or_ex(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id)
    return "GX" in subs or "EX" in subs


async def black_ray_gx(ctx):
    for target in [p for p in ctx.opponent_pokemon_in_play() if _is_gx_or_ex(p)]:
        await ctx.deal_damage(100, target=target, ignore_weakness=True,
                              ignore_resistance=True)


card = PokemonCardDef(
    guid="0daf7c37-97ff-5d88-818c-a4536421132f",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NecrozmaGX.Name",
    display_name="Necrozma-GX",
    searchable_by=["Necrozma-GX", "Basic", "GX", "NecrozmaGX"],
    subtypes=["Basic", "GX"],
    collector_number=63,
    set_code="SM3",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Ability(
            title="Light's End",
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's [C] Pokémon.",
            passive=LightsEndPassive(),
        ),
        Attack(
            title="Prism Burst",
            game_text="Discard all [P] Energy from this Pokémon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            effect=prism_burst,
        ),
        Attack(
            title="Black Ray-GX",
            game_text="This attack does 100 damage to each of your opponent's Pokémon-GX and Pokémon-EX. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=0,
            gx=True,
            effect=black_ray_gx,
        ),
    ],
)
