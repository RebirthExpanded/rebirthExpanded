"""Mime Jr. (SV045 31 -- JP SV4a 085; English PAF/157, PAF/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for as _def_for


async def mimed_games(ctx):
    candidates = [(p, a) for p in ctx.opponent_pokemon_in_play()
                  for a in getattr(_def_for(p.archetype_id), "abilities", []) if isinstance(a, Attack)]
    if not candidates:
        return
    index = await ctx.choose("Choose an attack for your opponent to use", [a.title for _p, a in candidates],
                             player_id=ctx.opponent_id)
    if isinstance(index, int) and 0 <= index < len(candidates):
        await ctx.use_attack(candidates[index][1])


card = PokemonCardDef(
    guid="c402cf42-cccf-55c4-b426-3b3611f7256c",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimeJr.Name",
    display_name="Mime Jr.",
    searchable_by=["Mime Jr.", "Basic"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=439,
    abilities=[
        Attack(
            title="Mimed Games",
            game_text="Your opponent chooses an attack from 1 of their Pokémon in play. Use the chosen attack as this attack.",
            cost={},
            effect=mimed_games,
        ),
    ],
)
