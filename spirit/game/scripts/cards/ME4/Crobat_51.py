"""Crobat (ME4 51 -- JP M4 050; English CRI/51, CRI/93, MEP/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _in_active(board, player_id, pokemon) -> bool:
    return board.active_pokemon(player_id) is pokemon and bool(board.find_player_area(player_id, "deck").children)


async def nighttime_maneuvers(ctx):
    picks = await ctx.search_deck(None, count=1, minimum=0, prompt="Choose a card to put on top of your deck.")
    await ctx.shuffle_deck()
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = PokemonCardDef(
    guid="529d130e-a196-5b24-b816-6e9bf724f177",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=51,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Nighttime Maneuvers",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may use this Ability. Search your deck for a card. Shuffle your deck, then put that card on top of it.",
            activation=Activations.ONCE_PER_TURN,
            condition=_in_active,
            effect=nighttime_maneuvers,
        ),
        Attack(
            title="Poison Sound Wave",
            game_text="Your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=80,
            effect=ac.condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)
