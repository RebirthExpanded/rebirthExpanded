from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers, def_for
from spirit.game.card_effects.support_common import remove_self_from_play


async def biting_spree(ctx):
    """Evolved from hand: 2 damage counters on each of 2 opposing Pokemon."""
    if not getattr(ctx, "evolved_from_hand", True):
        return
    pool = ctx.opponent_pokemon_in_play()
    if not pool or not await ctx.ask_yes_no("Put 2 damage counters on each of 2 of your opponent's Pokémon?"):
        return
    count = min(2, len(pool))
    picks = await ctx.choose_cards(pool, count, minimum=count,
                                   prompt="Choose 2 of your opponent's Pokémon")
    for target in picks:
        await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="772e82a6-89d2-5dad-8c77-aa9166df2e0b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsCrobatex.Name",
    display_name="Team Rocket's Crobat ex",
    searchable_by=["Team Rocket's Crobat ex", "Stage 2", "ex", "TeamRocketsCrobatex"],
    subtypes=["Stage 2", "ex"],
    collector_number=122,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGolbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Biting Spree",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may choose 2 of your opponent's Pok\u00e9mon and put 2 damage counters on each of them.",
            trigger=Triggers.ON_EVOLVE,
            effect=biting_spree,
        ),
        Attack(
            title="Assassin's Return",
            game_text="You may put this Pok\u00e9mon into your hand. (Discard all cards attached to this Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2},
            damage=120,
            effect=remove_self_from_play("hand", with_attachments="discard", optional=True, prompt="Put this Pokémon into your hand?"),
        ),
    ],
)
