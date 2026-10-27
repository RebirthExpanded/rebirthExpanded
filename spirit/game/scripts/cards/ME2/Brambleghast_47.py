"""Brambleghast (ME2 47 -- JP M2 041; English PFL/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def prison_panic(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    target = ctx.opponent_active()
    if target is None or not await ctx.ask_yes_no("Use Prison Panic?"):
        return
    await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="9f638e42-8fc4-5c64-a8fb-8c4441972410",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brambleghast.Name",
    display_name="Brambleghast",
    searchable_by=["Brambleghast", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    family_id=946,
    abilities=[
        Ability(
            title="Prison Panic",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Make your opponent's Active Pokémon Confused.",
            trigger=Triggers.ON_EVOLVE,
            effect=prison_panic,
        ),
        Attack(
            title="Psychic Sphere",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
