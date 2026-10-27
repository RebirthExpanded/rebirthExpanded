"""Espeon (ME6A 58 -- JP M6a 058; English 30C/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_evolution_pokemon


async def miraculous_shine(ctx):
    for p in list(ctx.opponent_pokemon_in_play()):
        if is_evolution_pokemon(p) and not ctx.effects_blocked(p):
            await ctx.devolve_pokemon(p, steps=1, destination="hand")


card = PokemonCardDef(
    guid="3dbddebc-645d-5c74-9d07-5c699854a948",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Miraculous Shine",
            game_text="Devolve each of your opponent's evolved Pokémon by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=miraculous_shine,
        ),
        Attack(
            title="Super Psy Bolt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
