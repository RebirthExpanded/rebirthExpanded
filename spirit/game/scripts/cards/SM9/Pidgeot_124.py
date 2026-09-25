"""Pidgeot (SM - Team Up 124/181 -- JP SM9 068/095).

Stage 2 Colorless Pokemon, evolves from Pidgeotto. HP 130, weakness
Lightning x2, resistance Fighting -20, no retreat cost.

  Whirlwind   [CC] 60  Your opponent switches their Active Pokemon with 1 of
                       their Benched Pokemon.
  Spin Storm  [CCC]    Your opponent puts their Active Pokemon and all cards
                       attached to it into their hand.

Both are effects on the Defending Pokemon: nothing happens if it is Knocked
Out by the damage or protected from attack effects. After Spin Storm the
opponent promotes a new Active (none left loses the game, Super Scoop Up's
shape).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.session.effects import full_stack
from spirit.game.data_utils import Attack, PokemonCardDef


def _defender_affected(ctx):
    defender = ctx.defender
    if defender is None or defender in ctx.knockouts or ctx.effects_blocked(defender):
        return None
    return defender


async def whirlwind(ctx):
    await ctx.deal_damage()
    if _defender_affected(ctx) is not None:
        await opponent_switches(ctx)


async def spin_storm(ctx):
    defender = _defender_affected(ctx)
    if defender is None:
        return
    await ctx.put_in_hand(full_stack(defender), reveal=False)
    opponent_id = ctx.opponent_id

    async def _promote():
        if not await ctx.session._promote_new_active(opponent_id):
            screen_name = ctx.session.players[opponent_id].screen_name
            await ctx.session.end_game(ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="154f3ee5-fb1d-53ee-8f75-ce28e31afb4c",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=['Pidgeot', 'Stage 2', 'Pidgeot'],
    subtypes=['Stage 2'],
    collector_number=124,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Attack(title="Whirlwind", game_text="Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.",
               cost={PokemonTypes.COLORLESS: 2}, damage=60,
               effect=whirlwind),
        Attack(title="Spin Storm", game_text="Your opponent puts their Active Pokémon and all cards attached to it into their hand.",
               cost={PokemonTypes.COLORLESS: 3}, damage=0,
               effect=spin_storm),
    ],
)
