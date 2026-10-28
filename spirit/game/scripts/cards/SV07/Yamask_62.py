"""Yamask (SV07 62 -- JP SV4K 030; English PAR/75, SCR/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def ominous_eyes(ctx):
    pool = ctx.opponent_pokemon_in_play()
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to put 3 damage counters on") if pool else None
    if target is not None:
        await ctx.deal_damage(30, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="d55c4f5d-44ad-5407-a34a-497f2a0aa119",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SV07",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=562,
    abilities=[
        Attack(
            title="Ominous Eyes",
            game_text="Put 3 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=ominous_eyes,
        ),
    ],
)
