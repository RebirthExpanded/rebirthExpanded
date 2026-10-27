"""Rotom (SV08 61 -- JP SV8 037; English SSP/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_item_card, is_pokemon_tool


async def crushing_pulse(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    junk = [c for c in hand if is_item_card(c) or is_pokemon_tool(c)]
    if junk:
        await ctx.discard_cards(junk)


card = PokemonCardDef(
    guid="ec3fc207-48ce-5a39-8f3e-c18cc0c953cd",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Crushing Pulse",
            game_text="Your opponent reveals their hand. Discard all Item cards and Pokémon Tool cards you find there.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=crushing_pulse,
        ),
        Attack(
            title="Energy Short",
            game_text="This attack does 20 damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("defender"), 20),
        ),
    ],
)
