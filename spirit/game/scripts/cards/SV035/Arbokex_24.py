"""Arbok ex (SV035 24 -- JP SV2a 024; English MEW/185, MEW/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def menacing_fangs(ctx):
    await ctx.deal_damage()
    hand = ctx.hand(ctx.opponent_id)
    k = min(2, len(hand))
    if k:
        await ctx.discard_from_hand(k, minimum=k, player_id=ctx.opponent_id, prompt=f"Discard {k} card(s) from your hand")


card = PokemonCardDef(
    guid="826e5f1d-329d-5fc0-a6cd-e3c788223269",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbokex.Name",
    display_name="Arbok ex",
    searchable_by=["Arbok ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=24,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Menacing Fangs",
            game_text="Your opponent discards 2 cards from their hand.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=150,
            effect=menacing_fangs,
        ),
    ],
)
