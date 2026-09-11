"""Dawn Wings Necrozma-GX (SM - Ultra Prism 63/156 -- JP SM5M 033/066).

Basic Psychic Pokemon-GX. HP 180, weakness Darkness x2, resistance
Fighting -20, retreat 2.

  Ability  Invasion  Once during your turn (before your attack), if this
                     Pokemon is on your Bench, you may switch it with your
                     Active Pokemon.
  Dark Flash  [PPP] 120  This attack's damage isn't affected by Resistance.
  Moon's Eclipse-GX  [PPP] 180  You can use this attack only if you have
                     more Prize cards remaining than your opponent. Prevent
                     all effects of attacks, including damage, done to this
                     Pokemon during your opponent's next turn.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack
from spirit.game.card_effects.passives_common import (apply_protection,
                                                       is_in_active_spot)
from spirit.game.card_effects.support_common import more_prizes_remaining_than_opponent
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


def _on_bench(board, player_id, pokemon) -> bool:
    return not is_in_active_spot(pokemon)


async def invasion(ctx):
    await ctx.switch_active(ctx.player_id, ctx.source)


async def dark_flash(ctx):
    await ctx.deal_damage(ignore_resistance=True)


async def moons_eclipse_gx(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="e3afa0ca-cb62-54da-bf0d-2eabb88f9a92",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DawnWingsNecrozmaGX.Name",
    display_name="Dawn Wings Necrozma-GX",
    searchable_by=["Dawn Wings Necrozma-GX", "Basic", "GX", "DawnWingsNecrozmaGX"],
    subtypes=["Basic", "GX"],
    collector_number=63,
    set_code="SM5",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=800,
    abilities=[
        Ability(
            title="Invasion",
            game_text="Once during your turn (before your attack), if this Pokémon is on your Bench, you may switch it with your Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench,
            effect=invasion,
        ),
        Attack(
            title="Dark Flash",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=dark_flash,
        ),
        Attack(
            title="Moon's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=180,
            gx=True,
            condition=more_prizes_remaining_than_opponent,
            effect=moons_eclipse_gx,
        ),
    ],
)
