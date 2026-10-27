"""Meowscarada (SV09 18 -- JP SV9 012; English JTG/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


def _on_bench(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bench is not None and pokemon.parent is bench


async def showtime(ctx):
    await ctx.switch_active(ctx.player_id, ctx.source)


card = PokemonCardDef(
    guid="b6fc82a1-53b9-505e-9aa6-680e026e734c",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscarada.Name",
    display_name="Meowscarada",
    searchable_by=["Meowscarada", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Ability(
            title="Showtime",
            game_text="Once during your turn, if this Pokémon is on your Bench, you may switch it with your Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench,
            effect=showtime,
        ),
        Attack(
            title="Rising Bloom",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex, 90),
        ),
    ],
)
