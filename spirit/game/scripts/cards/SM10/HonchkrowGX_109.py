"""Honchkrow-GX (SM - Unbroken Bonds 109/214 -- JP SM10 056/095, the art
here).

Stage 1 Darkness Pokemon-GX (evolves from Murkrow). HP 210, weakness
Lightning x2, resistance Fighting -20, retreat 2. When Knocked Out, the
opponent takes 2 Prize cards.

  Ruler of the Night  (Ability)  As long as this Pokemon is your Active
                                 Pokemon, your opponent can't play any
                                 Pokemon Tool, Special Energy, or Stadium
                                 cards from their hand.
  Feather Storm       [DCC] 90   This attack does 30 damage to 2 of your
                                 opponent's Benched Pokemon-GX and
                                 Pokemon-EX.
  Unfair-GX           [CC]       Your opponent reveals their hand. Discard
                                 2 cards from it.

Ruler of the Night is a hand-play block (Stoutland's Sentinel shape) that
names Tools, Stadiums and Special Energy; the legal-action builder asks
it of Energy cards too. "Pokemon-EX" is the XY-era uppercase EX.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.session.passives import Passive


class RulerOfTheNightPassive(Passive):
    """Active only: the opponent plays no Tool, Stadium or Special Energy from hand."""

    def blocks_trainer_play(self, card, player_id, carrier):
        if player_id == carrier.owning_player_id or not is_in_active_spot(carrier):
            return False
        if card.get_attribute(AttrID.TRAINER_TYPE) in (
                TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
                TrainerType.STADIUM.value):
            return True
        return bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def _benched_gx_or_ex(pokemon) -> bool:
    return (not is_in_active_spot(pokemon)
            and any(s in ("GX", "EX") for s in subtypes_for(pokemon.archetype_id)))


async def unfair_gx(ctx):
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 2, minimum=min(2, len(hand)),
        prompt="Choose 2 cards to discard from your opponent's hand.")
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="5f509a46-0b0e-537d-8482-1973aef7b930",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HonchkrowGX.Name",
    display_name="Honchkrow-GX",
    searchable_by=["Honchkrow-GX", "Stage 1", "GX", "HonchkrowGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=109,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Ability(
            title="Ruler of the Night",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent can't play any Pokémon Tool, Special Energy, or Stadium cards from their hand.",
            passive=RulerOfTheNightPassive(),
        ),
        Attack(
            title="Feather Storm",
            game_text="This attack does 30 damage to 2 of your opponent's Benched Pokémon-GX and Pokémon-EX. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=snipe_attack(30, pool=_benched_gx_or_ex, count=2, also_base=True),
        ),
        Attack(
            title="Unfair-GX",
            game_text="Your opponent reveals their hand. Discard 2 cards from it. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            gx=True,
            effect=unfair_gx,
        ),
    ],
)
