"""Gyarados (SV035 130 -- JP SV2a 130; English MEW/130). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def untamed_one(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    top = list(ctx.deck_top(5))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="827e4c5c-f56a-5cdb-a895-4379b28c9ed3",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=130,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Ability(
            title="Untamed One",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you must discard the top 5 cards of your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=untamed_one,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=ac.discard_opponent_energy_attack(1),
        ),
    ],
)
