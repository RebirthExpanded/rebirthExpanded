"""Hypno (SV035 97 -- JP SV2a 097; English MEW/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def here_for_hypnosis(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    d = ctx.opponent_active()
    if d is None or not await ctx.ask_yes_no("Use Here for Hypnosis?"):
        return
    await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="ab437285-8cc3-540e-9bae-462ba4b90c9b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=97,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Ability(
            title="Here for Hypnosis",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may make your opponent's Active Pokémon Asleep.",
            trigger=Triggers.ON_EVOLVE,
            effect=here_for_hypnosis,
        ),
        Attack(
            title="Super Psy Bolt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
