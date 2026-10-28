"""Camerupt (SV3 32 -- JP SV2D 011; English OBF/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_card


async def eruption(ctx):
    top = []
    for pid in (ctx.player_id, ctx.opponent_id):
        top += list(ctx.deck_top(1, player_id=pid))
    if top:
        await ctx.discard_cards(top)
    n = sum(1 for c in top if is_energy_card(c))
    await ctx.deal_damage(50 + 100 * n)


card = PokemonCardDef(
    guid="ac4a898b-b220-51fa-8749-e749250bbcec",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name",
    display_name="Camerupt",
    searchable_by=["Camerupt", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Eruption",
            game_text="Discard the top card of each player's deck. This attack does 100 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=eruption,
        ),
        Attack(
            title="Steaming Stomp",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
