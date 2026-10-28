"""Finizen (SV3 60 -- JP SV3 029; English OBF/60, PAF/123). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def _evolve_from_deck(ctx, pokemon) -> bool:
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return False
    picks = await ctx.search_deck(
        lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
        count=1, minimum=0, prompt="Choose a card that evolves from this Pokémon.")
    if picks:
        await ctx.evolve_pokemon(pokemon, picks[0])
        return True
    return False


async def valiant_evolution(ctx):
    bench = ctx.my_bench()
    me = ctx.attacker
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
    if target is None or not await ctx.switch_active(ctx.player_id, target):
        return
    await _evolve_from_deck(ctx, me)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="4f32b416-b222-577e-a657-f1ebb8c07619",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    display_name="Finizen",
    searchable_by=["Finizen", "Basic"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=963,
    abilities=[
        Attack(
            title="Valiant Evolution",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=valiant_evolution,
        ),
        Attack(
            title="Razor Fin",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
