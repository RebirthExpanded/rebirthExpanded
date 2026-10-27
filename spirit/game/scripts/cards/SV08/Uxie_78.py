"""Uxie (SV08 78 -- JP SV8 048; English SSP/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def painful_memories(ctx):
    for p in list(ctx.opponent_pokemon_in_play()):
        await ctx.deal_damage(20, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="07d58839-c0f8-58a4-8765-fd1016d9143a",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    display_name="Uxie",
    searchable_by=["Uxie", "Basic"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=480,
    abilities=[
        Attack(
            title="Painful Memories",
            game_text="Put 2 damage counters on each of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=painful_memories,
        ),
    ],
)
