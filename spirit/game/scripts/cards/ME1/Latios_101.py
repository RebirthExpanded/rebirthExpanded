"""Latios (ME1 101 -- JP M1S 050; English MEG/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _lustrous_applies(ctx) -> bool:
    moved = getattr(ctx, "moved_pokemon", None)
    return (moved is not None and ctx.source._containing_area_name() == "bench"
            and getattr(def_for(moved.archetype_id), "display_name", "") == "Mega Latias ex")


async def lustrous_assist(ctx):
    me = ctx.source
    state = ctx.session.turn_state
    if ctx.moved_pokemon is None:
        return
    if getattr(me, "_lustrous_turn", None) == state.turn_number:
        return
    active = ctx.board.active_pokemon(ctx.player_id)
    if active is None or not any(ctx.attached_energies(p) for p in ctx.my_bench()):
        return
    if not await ctx.ask_yes_no("Use Lustrous Assist?"):
        return
    me._lustrous_turn = state.turn_number
    pool = [e for p in ctx.my_bench() for e in ctx.attached_energies(p)]
    picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Choose any amount of Energy to move to your Active Pokémon")
    for energy in picks:
        await ctx.move_energy(energy, active)


card = PokemonCardDef(
    guid="3d7d8fb1-1a71-5dc0-b4ca-22ed304532bc",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=381,
    abilities=[
        Ability(
            title="Lustrous Assist",
            game_text="Once during your turn, when your Mega Latias ex moves from your Bench to the Active Spot, you may use this Ability. Move any amount of Energy from your Benched Pokémon to your Active Pokémon.",
            trigger=Triggers.ON_ALLY_MOVE_TO_ACTIVE,
            trigger_applies=_lustrous_applies,
            effect=lustrous_assist,
        ),
        Attack(
            title="Dragon Claw",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
