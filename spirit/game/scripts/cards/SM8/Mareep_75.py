"""Mareep (SM - Lost Thunder 75/214 -- JP SM8 033/095, the art here).

Basic Lightning Pokemon. HP 50, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Ability  Fluffy Pillow  Once during your turn (before your attack), if
                          this Pokemon is your Active Pokemon, you may
                          leave your opponent's Active Pokemon Asleep.
  Tackle [CC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


def _fluffy_pillow_condition(board, player_id, pokemon) -> bool:
    if not is_in_active_spot(pokemon):
        return False
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    return opponent is not None and board.active_pokemon(opponent) is not None


async def fluffy_pillow(ctx):
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="eb245f9b-77fb-55d6-b2b5-857f80b05e0e",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    display_name="Mareep",
    searchable_by=["Mareep", "Basic"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=179,
    abilities=[
        Ability(title="Fluffy Pillow",
                game_text="Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may leave your opponent's Active Pokémon Asleep.",
                activation=Activations.ONCE_PER_TURN,
                condition=_fluffy_pillow_condition,
                effect=fluffy_pillow),
        Attack(title="Tackle", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
