"""Azumarill ex (ME2PT5 84 -- JP MC 297; English ASC/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _others_with_energy(ctx, me):
    return [p for p in ctx.my_pokemon_in_play() if p is not me and ctx.attached_energies(p)]


def _can_gather(board, player_id, pokemon) -> bool:
    return any(p is not pokemon and board.attached_energies(p) for p in board.pokemon_in_play(player_id))


async def bubble_gathering(ctx):
    me = ctx.source
    donors = _others_with_energy(ctx, me)
    if not donors:
        return
    pool = [e for p in donors for e in ctx.attached_energies(p)]
    picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Choose an Energy to move to this Pokémon")
    if picks:
        await ctx.move_energy(picks[0], me)


card = PokemonCardDef(
    guid="13032c0d-d92b-5bcb-a74e-29a5e16bf02a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarillex.Name",
    display_name="Azumarill ex",
    searchable_by=["Azumarill ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=84,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=298,
    abilities=[
        Ability(
            title="Bubble Gathering",
            game_text="As often as you like during your turn, you may use this Ability. Move an Energy from 1 of your other Pokémon to this Pokémon.",
            activation=Activations.UNLIMITED,
            condition=_can_gather,
            effect=bubble_gathering,
        ),
        Attack(
            title="Energized Balloon",
            game_text="This attack does 40 more damage for each Psychic Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", PokemonTypes.PSYCHIC), 40, base=60),
        ),
    ],
)
