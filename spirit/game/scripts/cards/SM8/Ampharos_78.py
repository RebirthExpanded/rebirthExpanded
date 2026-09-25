"""Ampharos (SM - Lost Thunder 78/214 -- JP SM8 036/095).

Stage 2 Lightning Pokemon, evolves from Flaaffy. HP 150, weakness Fighting
x2, resistance Metal -20, retreat 2.

  Ability  Unseen Flash  Once during your turn (before your attack), you may
                         put 2 [L] Energy cards from your hand in the Lost
                         Zone. If you do, your opponent's Active Pokemon is
                         now Paralyzed.
  Split Bomb  [LL]       This attack does 50 damage to 2 of your opponent's
                         Pokemon.

Unseen Flash needs 2 [L] Energy cards in hand (it is not offered with
fewer). Split Bomb applies Weakness/Resistance to the Active only.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.session.effects import is_energy_of_type
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


def _lightning_energy_cards(cards):
    return [c for c in cards if is_energy_of_type(c, PokemonTypes.LIGHTNING)]


def _unseen_flash_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return len(_lightning_energy_cards(hand.children if hand else [])) >= 2


async def unseen_flash(ctx):
    cards = _lightning_energy_cards(ctx.hand())
    if len(cards) < 2:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=2, prompt="Choose 2 Lightning Energy cards to put in the Lost Zone")
    if not picks or len(picks) < 2:
        return
    await ctx.move_to_lost_zone(picks)
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="6324fa3a-908d-5bf7-b240-c6b5db994ecc",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=['Ampharos', 'Stage 2', 'Ampharos'],
    subtypes=['Stage 2'],
    collector_number=78,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Unseen Flash",
            game_text="Once during your turn (before your attack), you may put 2 Lightning Energy cards from your hand in the Lost Zone. If you do, your opponent's Active Pokémon is now Paralyzed.",
            activation=Activations.ONCE_PER_TURN,
            condition=_unseen_flash_condition,
            effect=unseen_flash,
        ),
        Attack(title="Split Bomb", game_text="This attack does 50 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
               cost={PokemonTypes.LIGHTNING: 2}, damage=0,
               effect=snipe_attack(50, pool="any", count=2)),
    ],
)
