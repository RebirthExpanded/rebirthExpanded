"""Team Rocket's Persian ex (SV10 150 -- JP SV10 079; English DRI/150, DRI/219, SVP/218). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.data_utils import def_for as _def_for
from spirit.game.session.effects import is_pokemon_card


async def haughty_order(ctx):
    top = list(ctx.deck_top(10, player_id=ctx.opponent_id))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    candidates = [(card, ability) for card in top if is_pokemon_card(card)
                  for ability in getattr(_def_for(card.archetype_id), "abilities", [])
                  if isinstance(ability, Attack)]
    picked = None
    if candidates and await ctx.ask_yes_no("Use an attack from a Pokémon you found?"):
        picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    await ctx.shuffle_deck(ctx.opponent_id)
    if picked is not None:
        await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="fcab4bc2-f305-592f-bbfa-d8d9e867bb98",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPersianex.Name",
    display_name="Team Rocket's Persian ex",
    searchable_by=["Team Rocket's Persian ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=150,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMeowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Haughty Order",
            game_text="Reveal the top 10 cards of your opponent's deck. You may choose an attack from a Pokémon you find there and use it as this attack. Shuffle the revealed cards into your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=haughty_order,
        ),
        Attack(
            title="Cruel Slash",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
