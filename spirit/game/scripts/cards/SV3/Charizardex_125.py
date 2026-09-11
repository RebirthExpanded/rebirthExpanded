"""Charizard ex (SV - Obsidian Flames 125/197 -- JP SV3 066/108).

Stage 2 Darkness Tera Pokemon ex, evolves from Charmeleon. HP 330,
weakness Grass x2, retreat 2.

  Tera  As long as this Pokemon is on your Bench, prevent all damage done
        to this Pokemon by attacks.
  Ability  Infernal Reign  When you play this Pokemon from your hand to
                           evolve 1 of your Pokemon during your turn, you
                           may search your deck for up to 3 Basic [R]
                           Energy cards and attach them to your Pokemon in
                           any way you like. Then, shuffle your deck.
  Burning Darkness  [RR] 180+  This attack does 30 more damage for each
                               Prize card your opponent has taken.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_taken, damage_per
from spirit.game.card_effects.pokemon import TeraRulePassive, energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    Triggers)
from spirit.game.session.effects import is_basic_energy


def _basic_fire_energy(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def infernal_reign(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not await ctx.ask_yes_no("Search your deck for up to 3 Basic [R] Energy cards to attach?"):
        return
    await search_attach_energy(_basic_fire_energy, count=3, distribute=True,
                               prompt="Choose up to 3 Basic [R] Energy cards to attach.")(ctx)


card = PokemonCardDef(
    guid="6c25094e-0490-54c2-afbf-a2e0650e128b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizardex.Name",
    display_name="Charizard ex",
    searchable_by=["Charizard ex", "Stage 2", "ex", "Tera", "Charizardex"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=125,
    set_code="SV3",
    rarity=Rarities.RareUltra,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    regulation_mark="G",
    passive=TeraRulePassive(),
    abilities=[
        Ability(title="Infernal Reign",
                game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may search your deck for up to 3 Basic [R] Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.",
                trigger=Triggers.ON_EVOLVE, effect=infernal_reign),
        Attack(title="Burning Darkness",
               game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
               cost={PokemonTypes.FIRE: 2}, damage=180,
               effect=damage_per(count_prizes_taken("opponent"), 30, base=180)),
    ],
)
