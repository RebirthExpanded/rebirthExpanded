from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.session.effects import full_stack


def _tr_energy(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Team Rocket's Energy"


async def evil_incineration(ctx):
    """Discard a Team Rocket's Energy from this Pokemon; if you do, discard
    the opponent's Active and all attached cards (not a Knock Out)."""
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _tr_energy(e)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, prompt="Discard a Team Rocket's Energy from this Pokémon")
    if not picks:
        return
    await ctx.discard_cards(picks)
    target = ctx.defender
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_cards(full_stack(target))

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)

card = PokemonCardDef(
    guid="bfa8094b-2bda-540f-86f4-1f3ce136f78a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMoltresex.Name",
    display_name="Team Rocket's Moltres ex",
    searchable_by=["Team Rocket's Moltres ex", "Basic", "ex", "TeamRocketsMoltresex"],
    subtypes=["Basic", "ex"],
    collector_number=31,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=146,
    abilities=[
        Attack(
            title="Flame Screen",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=protect_next_turn(reduce=50),
        ),
        Attack(
            title="Evil Incineration",
            game_text="Discard a Team Rocket's Energy from this Pok\u00e9mon. If you do, discard your opponent's Active Pok\u00e9mon and all attached cards.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=0,
            effect=evil_incineration,
        ),
    ],
)
