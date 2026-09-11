"""Raichu (SM - Burning Shadows 41/147 -- JP SM3N 014/051).

Stage 1 Lightning Pokemon, evolves from Pikachu. HP 110, weakness
Fighting x2, resistance Metal -20, retreat 1.

  Ability  Evoshock  When you play this Pokemon from your hand to evolve 1
                     of your Pokemon during your turn, you may leave your
                     opponent's Active Pokemon Paralyzed.
  Volt Tackle  [LLC] 130  This Pokemon does 30 damage to itself.

Evoshock reads the ctx's evolved_from_hand flag, so a deck-sourced
evolution (Wally) does not fire it; a shielded Active is not Paralyzed.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    Triggers)


async def evoshock(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    if await ctx.ask_yes_no("Leave your opponent's Active Pokémon Paralyzed?"):
        await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="21dd9655-9216-5d65-a25f-82143575062f",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Evoshock",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may leave your opponent's Active Pokémon Paralyzed.",
            trigger=Triggers.ON_EVOLVE,
            effect=evoshock,
        ),
        Attack(
            title="Volt Tackle",
            game_text="This Pokémon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=recoil_attack(30),
        ),
    ],
)
