"""Gloom (SV035 44 -- JP SV2a 044; English MEW/44, PAF/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


async def semi_blooming_energy(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not ctx.deck_top(1) or not await ctx.ask_yes_no("Use Semi-Blooming Energy?"):
        return
    await su.look_top_attach_energy(3, predicate=is_basic_energy_card)(ctx)


card = PokemonCardDef(
    guid="8802d057-3293-5633-9590-959add1f1e21",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Semi-Blooming Energy",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may look at the top 3 cards of your deck and attach any number of Basic Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=semi_blooming_energy,
        ),
        Attack(
            title="Drool",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
