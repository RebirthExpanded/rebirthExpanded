"""Sylveon (Promo_SWSH 211 -- JP SP 237; English SP/211). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _time_out_kick(ctx):
    """You may put an Energy attached to the opponent's Active into their hand."""
    await ctx.deal_damage()
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    if not await ctx.ask_yes_no("Put an Energy attached to your opponent's Active Pokémon into their hand?"):
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy to put into your opponent's hand.")
    await ctx.put_in_hand(picks, reveal=False)
from spirit.game.card_effects import attacks_common as ac



def _supporter_played(ctx) -> bool:
    return ctx.supporters_played_this_turn() > 0


card = PokemonCardDef(
    guid="d799f787-488e-56ea-bef7-a486cc61bae7",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=211,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Time Out Kick",
            game_text="You may put an Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=_time_out_kick,
        ),
        Attack(
            title="Symphony Whip",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_supporter_played, 70),
        ),
    ],
)
