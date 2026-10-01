from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID, SpecialConditions, TrainerType
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class TrappingThreadPassive(Passive):
    """Rides the Defending Pokemon through the opponent's next turn: the
    Items and Supporters they play from hand have no effect on it. Welder
    can still be played, but Fire Energy it would attach to this Pokemon is
    discarded, and with nothing attached it draws nothing (ruling)."""

    def blocks_own_trainer_effect(self, target, trainer_card, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or target is not holder:
            return False
        if trainer_card.owning_player_id != holder.owning_player_id:
            return False
        return trainer_card.get_attribute(AttrID.TRAINER_TYPE) in (
            TrainerType.ITEM.value, TrainerType.SUPPORTER.value)


async def trapping_thread(ctx):
    """30, then the Defending Pokemon is out of reach of its owner's Items
    and Supporters during their next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(defender, TrappingThreadPassive())

card = PokemonCardDef(
    guid="43c9e0fd-d017-5583-83a8-e9a287c2f5e0",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Attack(
            title="Trapping Thread",
            game_text="Whenever your opponent plays an Item or Supporter card from their hand during their next turn, prevent all effects of that card done to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=trapping_thread,
        ),
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
