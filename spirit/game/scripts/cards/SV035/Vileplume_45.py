"""Vileplume (SV035 45 -- JP SV2a 045; English MEW/45, PAF/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


async def fully_blooming_energy(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not ctx.deck_top(1) or not await ctx.ask_yes_no("Use Fully Blooming Energy?"):
        return
    await su.look_top_attach_energy(8, predicate=is_basic_energy_card)(ctx)


card = PokemonCardDef(
    guid="1bdb2180-51e5-5aa6-a505-d284a9924639",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Fully Blooming Energy",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may look at the top 8 cards of your deck and attach any number of Basic Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=fully_blooming_energy,
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
