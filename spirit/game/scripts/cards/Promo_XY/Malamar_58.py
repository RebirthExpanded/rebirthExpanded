"""Malamar (XY Black Star Promo 58 -- JP XY-P 130, the art here).

Stage 1 Darkness Pokemon (evolves from Inkay). HP 90, weakness Fighting
x2, resistance Psychic -20, retreat 2.

  Theta Stop  (Ancient Trait)  Prevent all effects of your opponent's
                               Pokemon's Abilities done to this Pokemon.
  Contrary    (Ability)        If this Pokemon is your Active Pokemon,
                               whenever your opponent flips a coin during
                               his or her turn, treat it as tails.
  Conform     [DCC] 40         If you have the same number of cards in
                               your hand as your opponent, your opponent's
                               Active Pokemon is now Confused.

Contrary answers Passive.forces_coin_tails: every coin the opponent flips
during their own turn (card effects, the Confusion / Smokescreen / attach-
tax flips) lands tails, applied AFTER Will's chosen result -- a heads the
opponent picked with Will is still a coin they flipped (ruling). The
Pokemon Checkup's Sleep and Burn flips are between turns and untouched.
Theta Stop is an Ancient Trait, so an Ability lock does not switch it off.
"""

from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import ability_effect_shield_passive, is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class ContraryPassive(Passive):
    """The opponent's in-turn coins are all tails while the carrier is Active."""

    def forces_coin_tails(self, flipper_id, carrier) -> bool:
        return flipper_id != carrier.owning_player_id and is_in_active_spot(carrier)


async def conform(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None and len(ctx.hand()) == len(ctx.hand(ctx.opponent_id)):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="e0b03fd3-ec90-548d-8eaf-e6dd77df9ac1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=687,
    abilities=[
        Ability(
            title="θ Stop",
            game_text="Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.",
            ability_type=AbilityTypes.ANCIENT_TRAIT,
            passive=ability_effect_shield_passive(),
        ),
        Ability(
            title="Contrary",
            game_text="If this Pokémon is your Active Pokémon, whenever your opponent flips a coin during his or her turn, treat it as tails.",
            passive=ContraryPassive(),
        ),
        Attack(
            title="Conform",
            game_text="If you have the same number of cards in your hand as your opponent, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=conform,
        ),
    ],
)
