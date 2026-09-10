"""Vileplume-GX (SM - Cosmic Eclipse 4/236).

Stage 2 Grass Pokemon-GX. HP 240, weakness Fire x2, no resistance,
retreat 2.

  Ability  Fragrant Flower Garden  Once during your turn (before your
                                   attack), you may heal 30 damage from
                                   each of your Pokemon.

  Massive Bloom          [GC] 180-  This attack does 10 less damage for
                                    each damage counter on this Pokemon.
  Allergic Explosion-GX  [G]    50  Your opponent's Active Pokemon is now
                                    Burned, Paralyzed, and Poisoned.

The heal is board-wide and needs somebody hurt to do anything, so that is
the Ability's condition. Massive Bloom counts the counters on the attacker
itself, which makes it a damage race Vileplume-GX loses as it takes hits:
damage_per with a negative step off a 180 base.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import (PokemonTypes, PokemonStage, Rarities,
                                    SpecialConditions, AttrID)
from spirit.game.card_effects.attacks_common import (damage_counters_on,
                                                     damage_per,
                                                     condition_attack)
from spirit.game.session.passives import effective_max_hp


def _someone_is_hurt(board, player_id, pokemon=None):
    return any(
        effective_max_hp(board, p) - p.get_attribute(AttrID.HP, 0) > 0
        for p in board.pokemon_in_play(player_id)
    )


async def fragrant_flower_garden(ctx):
    """30 off every one of your Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(30, pokemon)


card = PokemonCardDef(
    guid="3b00f91a-03f2-53f1-97fb-76228bedde85",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplumegx.Name",
    display_name="Vileplume-GX",
    searchable_by=["Vileplume-GX", "Stage 2", "GX", "Vileplumegx"],
    subtypes=["Stage 2", "GX"],
    collector_number=4,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Fragrant Flower Garden",
            game_text=("Once during your turn (before your attack), you may "
                       "heal 30 damage from each of your Pokémon."),
            activation=Activations.ONCE_PER_TURN,
            condition=_someone_is_hurt,
            effect=fragrant_flower_garden,
        ),
        Attack(
            title="Massive Bloom",
            game_text=("This attack does 10 less damage for each damage "
                       "counter on this Pokémon."),
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=180,
            damage_operator="-",
            effect=damage_per(damage_counters_on("self"), -10, base=180),
        ),
        Attack(
            title="Allergic Explosion-GX",
            game_text=("Your opponent's Active Pokémon is now Burned, "
                       "Paralyzed, and Poisoned. (You can't use more than 1 "
                       "GX attack in a game.)"),
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            gx=True,
            effect=condition_attack(SpecialConditions.BURNED,
                                    SpecialConditions.PARALYZED,
                                    SpecialConditions.POISONED),
        ),
    ],
)
