"""Zeraora-GX (SM - Lost Thunder 86/214 -- JP SM7a 033/060, the art here).

Basic Lightning Pokemon-GX. HP 190, weakness Fighting x2, resistance Metal
-20, retreat 2.

  Ability: Thunderclap Zone  Each of your Pokemon that has any [L] Energy
                             attached to it has no Retreat Cost.
  Plasma Fists    [LLC] 160  This Pokemon can't attack during your next turn.
  Full Voltage-GX [L]        Attach 5 basic Energy cards from your discard
                             pile to your Pokemon in any way you like.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.models.board import board_of


def _has_lightning(pokemon, carrier) -> bool:
    if pokemon.owning_player_id != carrier.owning_player_id:
        return False
    board = board_of(pokemon)
    energies = board.attached_energies(pokemon) if board is not None else []
    return any(energy_provides_type(e, PokemonTypes.LIGHTNING.value) for e in energies)


async def plasma_fists(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


async def full_voltage_gx(ctx):
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, min(5, len(pool)), minimum=min(5, len(pool)),
        prompt="Choose 5 basic Energy cards to attach to your Pokémon")
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


card = PokemonCardDef(
    guid="2503d9ad-50a8-5183-b858-6626632b3d26",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraGX.Name",
    display_name="Zeraora-GX",
    searchable_by=["Zeraora-GX", "Basic", "GX", "ZeraoraGX"],
    subtypes=["Basic", "GX"],
    collector_number=86,
    set_code="SM8",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=807,
    abilities=[
        Ability(
            title="Thunderclap Zone",
            game_text="Each of your Pokémon that has any [L] Energy attached to it has no Retreat Cost.",
            passive=retreat_free_when(_has_lightning),
        ),
        Attack(
            title="Plasma Fists",
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=plasma_fists,
        ),
        Attack(
            title="Full Voltage-GX",
            game_text="Attach 5 basic Energy cards from your discard pile to your Pokémon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            gx=True,
            effect=full_voltage_gx,
        ),
    ],
)
