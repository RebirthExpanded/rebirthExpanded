"""Clawitzer (ME1 38 -- JP M1S 020; English MEG/141, MEG/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_water(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.WATER)


async def fall_back_to_reload(ctx):
    me = ctx.source
    state = ctx.session.turn_state
    if getattr(me, "_reload_turn", None) == state.turn_number:
        return
    pool = [c for c in ctx.hand() if _basic_water(c)]
    if not pool or not await ctx.ask_yes_no("Use Fall Back to Reload?"):
        return
    me._reload_turn = state.turn_number
    picks = await ctx.choose_cards(pool, 2, minimum=0, prompt="Attach up to 2 Basic Water Energy cards to this Pokémon")
    for card in picks:
        await ctx.attach_energy(card, me)


card = PokemonCardDef(
    guid="70d2490a-80f9-516c-93e2-d8fd861fe1b6",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    display_name="Clawitzer",
    searchable_by=["Clawitzer", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    family_id=692,
    abilities=[
        Ability(
            title="Fall Back to Reload",
            game_text="Once during your turn, when this Pokémon moves from the Active Spot to your Bench, you may use this Ability. Attach up to 2 Basic Water Energy cards from your hand to this Pokémon.",
            trigger=Triggers.ON_MOVE_TO_BENCH,
            effect=fall_back_to_reload,
        ),
        Attack(
            title="Aqua Launcher",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 3},
            damage=210,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
