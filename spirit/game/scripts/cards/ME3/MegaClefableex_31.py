"""Mega Clefable ex (ME - Perfect Order 31 -- JP M3 030, the art here).

Stage 1 Psychic Mega Evolution Pokemon ex, evolves from Clefairy. HP 320,
weakness Metal x2, no resistance, retreat 1. Knocked Out: 3 Prize cards
(the SV_Mega subtype carries that).

  Ability  Luminous Wing  Prevent all effects of your opponent's Pokemon's
                          Abilities done to this Pokemon.
  Shooting Moons [PP] 120+  You may discard up to 4 Energy cards from your
                            hand, and this attack does 40 more damage for
                            each card you discarded in this way.

Luminous Wing is Stealthy Hood's shield as an Ability: it also keeps
Garbotoxin / Initialize off this Pokemon whichever came first (official
Q&A, wired in passives._locks_abilities_of), while a Stadium lock (Path
to the Peak -- it has a Rule Box) still reaches it.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import ability_effect_shield_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_energy_card


async def shooting_moons(ctx):
    """120, +40 per Energy card discarded from hand (up to 4, optional)."""
    energies = [c for c in ctx.hand() if is_energy_card(c)]
    bonus = 0
    if energies:
        picks = await ctx.discard_from_hand(
            min(4, len(energies)), minimum=0, predicate=is_energy_card,
            prompt="Discard up to 4 Energy cards from your hand (+40 each)")
        bonus = 40 * len(picks or [])
    await ctx.deal_damage(120 + bonus)


card = PokemonCardDef(
    guid="ac702c13-238c-5415-896b-87dcfcf10932",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaClefableex.Name",
    display_name="Mega Clefable ex",
    searchable_by=["Mega Clefable ex", "Stage 1", "ex", "SV_Mega", "MegaClefableex"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=31,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Ability(title="Luminous Wing",
                game_text="Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.",
                passive=ability_effect_shield_passive()),
        Attack(title="Shooting Moons",
               game_text="You may discard up to 4 Energy cards from your hand, and this attack does 40 more damage for each card you discarded in this way.",
               cost={PokemonTypes.PSYCHIC: 2},
               damage=120, damage_operator="+", effect=shooting_moons),
    ],
)
