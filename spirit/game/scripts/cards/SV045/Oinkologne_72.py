"""Oinkologne (SV045 72 -- JP SV3 098; English OBF/184, PAF/208, PAF/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def finest_selection(ctx):
    heads = sum(1 for r in await ctx.flip_coins(3, "Finest Selection") if r)
    discard = list(ctx.discard_pile())
    if heads and discard:
        picks = await ctx.choose_cards(discard, min(heads, len(discard)), minimum=0, prompt=f"Choose up to {heads} cards")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="c63af656-7f24-5e8a-b58d-a264d6defe3f",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name",
    display_name="Oinkologne",
    searchable_by=["Oinkologne", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    family_id=915,
    abilities=[
        Attack(
            title="Finest Selection",
            game_text="Flip 3 coins. Put a number of cards up to the number of heads from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=finest_selection,
        ),
        Attack(
            title="Perfume Press",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
