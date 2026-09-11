"""Brute Bonnet (SV - Paradox Rift 123/182 -- JP SV8a 099/187, the art here).

Basic Darkness Pokemon (Ancient). HP 120, weakness Grass x2, retreat 3.

  Ability  Toxic Powder  Once during your turn, if this Pokemon has an
                         Ancient Booster Energy Capsule attached, you may
                         make both Active Pokemon Poisoned.
  Rampaging Hammer  [DDC] 120  During your next turn, this Pokemon can't
                               attack.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef, def_for)


def _has_ancient_capsule(pokemon) -> bool:
    return any(getattr(def_for(c.archetype_id), "display_name", "") == "Ancient Booster Energy Capsule"
               for c in pokemon.children)


def _toxic_powder_condition(board, player_id, pokemon) -> bool:
    return _has_ancient_capsule(pokemon)


async def toxic_powder(ctx):
    for target in (ctx.my_active(), ctx.opponent_active()):
        if target is not None:
            await ctx.apply_special_condition(target, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="421266b3-020f-5c08-a52e-ae4c5c189ae7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BruteBonnet.Name",
    display_name="Brute Bonnet",
    searchable_by=["Brute Bonnet", "Basic", "Ancient", "BruteBonnet"],
    subtypes=["Basic", "Ancient"],
    collector_number=123,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=986,
    regulation_mark="G",
    abilities=[
        Ability(title="Toxic Powder",
                game_text="Once during your turn, if this Pokémon has an Ancient Booster Energy Capsule attached, you may make both Active Pokémon Poisoned.",
                activation=Activations.ONCE_PER_TURN, condition=_toxic_powder_condition,
                effect=toxic_powder),
        Attack(title="Rampaging Hammer", game_text="During your next turn, this Pokémon can't attack.",
               cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1}, damage=120,
               locks_next_turn=True),
    ],
)
