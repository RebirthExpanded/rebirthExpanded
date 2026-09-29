from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.pokemon import in_active_spot


def _auto_heal_applies(ctx) -> bool:
    """Active, and I attached from hand to 1 of my Pokemon still in play."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return False
    if ctx.attaching_player_id != ctx.player_id:
        return False
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id != ctx.player_id:
        return False
    return receiver in ctx.board.pokemon_in_play(ctx.player_id)


async def auto_heal(ctx):
    """Heal 90 from the Pokemon I just attached an Energy card to from hand.
    When Gnawing Curse (or another trigger) goes off on the same attachment,
    I choose which resolves first."""
    if _auto_heal_applies(ctx):
        await ctx.heal(90, ctx.energy_receiver)


async def spike_draw(ctx):
    """20. Draw 2 cards."""
    await ctx.deal_damage()
    await ctx.draw_cards(2)

card = PokemonCardDef(
    guid="566ecf7e-ce34-58c6-ac51-c6fae3437e32",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magearna.Name",
    display_name="Magearna",
    searchable_by=["Magearna", "Basic", "Magearna"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=801,
    abilities=[
        Ability(
            title="Auto Heal",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, whenever you attach an Energy card from your hand to 1 of your Pok\u00e9mon, heal 90 damage from that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=auto_heal,
            trigger_applies=_auto_heal_applies,
        ),
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=spike_draw,
        ),
    ],
)
