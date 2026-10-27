"""Grumpig (ME1 63 -- JP M1S 045; English MEG/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


async def energized_steps(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if not ctx.deck_top(1) or not await ctx.ask_yes_no("Use Energized Steps?"):
        return
    await su.look_top_attach_energy(4, predicate=is_basic_energy_card)(ctx)


card = PokemonCardDef(
    guid="8a337b97-0b67-568d-acd9-40cec044ec27",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name",
    display_name="Grumpig",
    searchable_by=["Grumpig", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    family_id=325,
    abilities=[
        Ability(
            title="Energized Steps",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Look at the top 4 cards of your deck and attach any number of Basic Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=energized_steps,
        ),
        Attack(
            title="Psychic Sphere",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
