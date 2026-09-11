"""Keldeo-EX (BW - Boundaries Crossed 49/149 -- JP BW6-Bc 019/059).

Basic Water Pokemon-EX. HP 170, weakness Grass x2, retreat 2.

  Ability  Rush In  Once during your turn (before your attack), if this
                    Pokemon is on your Bench, you may switch it with your
                    Active Pokemon.
  Secret Sword  [CCC] 50+  Does 20 more damage for each [W] Energy attached
                           to this Pokemon.

Secret Sword counts Energy (provided [W]), so a Double Colorless adds
nothing and a card providing two [W] adds 40.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


def _on_bench(board, player_id, pokemon) -> bool:
    return not is_in_active_spot(pokemon)


async def rush_in(ctx):
    await ctx.switch_active(ctx.player_id, ctx.source)


card = PokemonCardDef(
    guid="5e235ef8-1e78-5d72-a024-d83df6a48ef7",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KeldeoEX.Name",
    display_name="Keldeo-EX",
    searchable_by=["Keldeo-EX", "Basic", "EX", "KeldeoEX"],
    subtypes=["Basic", "EX"],
    collector_number=49,
    set_code="BW7",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Ability(
            title="Rush In",
            game_text="Once during your turn (before your attack), if this Pokémon is on your Bench, you may switch it with your Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench,
            effect=rush_in,
        ),
        Attack(
            title="Secret Sword",
            game_text="Does 20 more damage for each [W] Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=damage_per(count_energy("self", PokemonTypes.WATER), 20, base=50),
        ),
    ],
)
