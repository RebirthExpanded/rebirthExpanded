"""Greninja-GX (SM Black Star Promo 197, Detective Pikachu -- JP SMP2
013/024, the art here).

Stage 2 Water Pokemon-GX (evolves from Frogadier). HP 230, weakness Grass
x2, no resistance, retreat 1. When Knocked Out, the opponent takes 2 Prizes.

  Elusive Master  (Ability)  Once during your turn (before your attack), if
                             this Pokemon is the last card in your hand,
                             you may play it onto your Bench. If you do,
                             draw 3 cards.
  Mist Slash      [WC] 130   This attack's damage isn't affected by
                             Weakness, Resistance, or any other effects on
                             your opponent's Active Pokemon.
  Dark Mist-GX    [W]        Put 1 of your opponent's Benched Pokemon and
                             all cards attached to it into your opponent's
                             hand. (You can't use more than 1 GX attack in
                             a game.)

Elusive Master is a hand Ability (bench_from_hand, Luxray's Swelling Flash
shape): offered as a Bench drop while Greninja-GX is the only card in
hand, and the draw is its ON_BENCHED_BY_ABILITY follow-up. Being an
Ability, Garbotoxin reaching the hand switches it off. Dark Mist-GX
returns the whole stack (attachments and pre-evolutions included).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers
from spirit.game.session.effects import full_stack


def _last_card_in_hand(board, player_id, card) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) == 1 and hand.children[0] is card


async def elusive_master_draw(ctx):
    await ctx.draw_cards(3)


async def dark_mist_gx(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon to put into their hand.")
    if target is not None:
        await ctx.put_in_hand(full_stack(target), reveal=False)


card = PokemonCardDef(
    guid="ac7787b5-6143-58ab-90ab-e42d1f25ef3c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaGX.Name",
    display_name="Greninja-GX",
    searchable_by=["Greninja-GX", "Stage 2", "GX", "GreninjaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=197,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=658,
    bench_from_hand=_last_card_in_hand,
    abilities=[
        Ability(
            title="Elusive Master",
            game_text="Once during your turn (before your attack), if this Pokémon is the last card in your hand, you may play it onto your Bench. If you do, draw 3 cards.",
            trigger=Triggers.ON_BENCHED_BY_ABILITY,
            effect=elusive_master_draw,
        ),
        Attack(
            title="Mist Slash",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
        Attack(
            title="Dark Mist-GX",
            game_text="Put 1 of your opponent's Benched Pokémon and all cards attached to it into your opponent's hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            gx=True,
            effect=dark_mist_gx,
        ),
    ],
)
