from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.effects import is_special_energy


def _has_special(ctx) -> bool:
    return any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))


async def startling_drop(ctx):
    """Milled by the opponent on their turn: discard the top 8 of their deck.
    The session only fires ON_DISCARDED_FROM_DECK for an attack, Ability,
    Item or Supporter of the opponent during the opponent's turn."""
    await ctx.discard_cards(ctx.deck_top(8, player_id=ctx.opponent_id))

card = PokemonCardDef(
    guid="28620256-ce12-5067-b9d6-7d05fb2891f3",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1", "Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Ability(
            title="Startling Drop",
            game_text="During your opponent's turn, if this Pok\u00e9mon is discarded from your deck by an effect of an attack or Ability from your opponent's Pok\u00e9mon, or by an effect of your opponent's Item or Supporter cards, discard the top 8 cards of your opponent's deck.",
            trigger=Triggers.ON_DISCARDED_FROM_DECK,
            effect=startling_drop,
        ),
        Attack(
            title="Special Whip",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 70 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=70,
            damage_operator="+",
            effect=bonus_if(_has_special, 70),
        ),
    ],
)
