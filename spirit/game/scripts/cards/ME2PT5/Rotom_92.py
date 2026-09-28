from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import full_stack, is_basic_pokemon, is_pokemon_tool


def _basic_rotom(card) -> bool:
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return is_basic_pokemon(card) and "Rotom" in name


async def gadget_show(ctx):
    """30 for each Pokemon Tool attached to all of your Pokemon."""
    tools = sum(1 for p in ctx.my_pokemon_in_play()
                for c in full_stack(p) if c is not p and is_pokemon_tool(c))
    if tools:
        await ctx.deal_damage(30 * tools)

card = PokemonCardDef(
    guid="674981e1-1545-5a1e-ba34-fbda62af0267",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=479,
    abilities=[
        Attack(
            title="Roto Call",
            game_text="You may search your deck for any number of Pok\u00e9mon that have \"Rotom\" in their name and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=search_to_bench(predicate=_basic_rotom, count=8, prompt="Choose any number of Rotom to put onto your Bench."),
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pok\u00e9mon Tool attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=gadget_show,
        ),
    ],
)
