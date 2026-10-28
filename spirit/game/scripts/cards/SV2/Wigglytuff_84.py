"""Wigglytuff (SV2 84 -- JP SV2D 027; English PAF/147, PAL/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _therapeutic(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == "Therapeutic Energy"


def _therapy_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_therapeutic(c) for c in hand.children)


async def balloon_therapy(ctx):
    pool = [c for c in ctx.hand() if _therapeutic(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Therapeutic Energy card to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon") if picks else None
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="283fcdb6-3d50-58bd-a9ff-3a0ab2a7e26e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=174,
    abilities=[
        Ability(
            title="Balloon Therapy",
            game_text="Once during your turn, you may attach a Therapeutic Energy card from your hand to 1 of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_therapy_condition,
            effect=balloon_therapy,
        ),
        Attack(
            title="Magical Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
