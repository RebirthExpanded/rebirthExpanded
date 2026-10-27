"""Mismagius ex (ME2 36 -- JP M2 036; English PFL/112, PFL/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import passives_common as pc


def _swirling_prose_applies(ctx) -> bool:
    moved = getattr(ctx, "moved_pokemon", None)
    return moved is not None and pc.is_in_active_spot(ctx.source) and pc.is_in_active_spot(moved)


async def swirling_prose(ctx):
    if ctx.moved_pokemon is None:
        return
    await ctx.apply_special_condition(ctx.moved_pokemon, SpecialConditions.CONFUSED)


async def hexa_magic(ctx):
    await ctx.deal_damage()
    if len(ctx.hand()) < 6 and await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="845b14b7-c9c1-513c-81ac-13b5f21908e5",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagiusex.Name",
    display_name="Mismagius ex",
    searchable_by=["Mismagius ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=36,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Ability(
            title="Swirling Prose",
            game_text="As long as this Pokémon is in the Active Spot, whenever your opponent's Active Pokémon moves to the Bench during their turn, their new Active Pokémon is now Confused.",
            trigger=Triggers.ON_OPPONENT_MOVE_TO_ACTIVE,
            trigger_applies=_swirling_prose_applies,
            effect=swirling_prose,
        ),
        Attack(
            title="Hexa-Magic",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=150,
            effect=hexa_magic,
        ),
    ],
)
