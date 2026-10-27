"""Hippowdon (ME3 40 -- JP M3 039; English POR/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _played_this_turn(ctx, display_name) -> bool:
    for archetype_id, _name, _type in ctx.session.turn_state.trainers_played:
        if getattr(def_for(archetype_id), "display_name", None) == display_name:
            return True
    return False


async def twister_spewing(ctx):
    await ctx.deal_damage()
    if _played_this_turn(ctx, "Tarragon"):
        await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="b4cd812c-1960-5409-b413-e003086bb026",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Twister Spewing",
            game_text="If you played Tarragon from your hand during this turn, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=twister_spewing,
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)
