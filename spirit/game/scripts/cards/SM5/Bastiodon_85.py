"""Bastiodon (SM - Ultra Prism 85/156 -- JP SM5S 039/066, the art here).

Stage 2 Metal Pokemon (evolves from Shieldon). HP 160, weakness Fire x2,
resistance Psychic -20, retreat 3.

  Earthen Shield  (Ability)  Prevent all damage done to your [M] Pokemon by
                             attacks from your opponent's Pokemon that
                             have any Special Energy attached to them.
  Push Down       [MMC] 110  You may have your opponent switch their
                             Active Pokemon with 1 of their Benched
                             Pokemon.

Earthen Shield reads the attacker's attachments at damage time: a Special
Energy anywhere under its stack counts. Two Bastiodon do not stack (a
prevention is a prevention).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_of_type, is_special_energy


def _earthen_shield(calc, carrier) -> bool:
    target, attacker = calc.target, calc.attacker
    if target is None or attacker is None:
        return False
    if target.owning_player_id != carrier.owning_player_id:
        return False
    if not is_pokemon_of_type(target, PokemonTypes.METAL):
        return False
    return any(is_special_energy(e) for e in calc.board.attached_energies(attacker))


async def push_down(ctx):
    await ctx.deal_damage()
    opp_active = ctx.opponent_active()
    if opp_active is None or not ctx.opponent_bench() or ctx.effects_blocked(opp_active):
        return
    if await ctx.ask_yes_no("Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        await opponent_switches(ctx)


card = PokemonCardDef(
    guid="9385d62a-b447-5468-82f3-61cbe5adc0ea",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=410,
    abilities=[
        Ability(
            title="Earthen Shield",
            game_text="Prevent all damage done to your [M] Pokémon by attacks from your opponent's Pokémon that have any Special Energy attached to them.",
            passive=prevent_damage_when(_earthen_shield),
        ),
        Attack(
            title="Push Down",
            game_text="You may have your opponent switch their Active Pokémon with 1 of their Benched Pokémon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=push_down,
        ),
    ],
)
