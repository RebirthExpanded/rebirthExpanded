"""Hypno (SV1 83 -- JP SV1V 039; English SVI/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for as _def_for


async def pendulum_influence(ctx):
    results = await ctx.flip_coins(1, "Pendulum Influence")
    if not (results and results[0]):
        return
    candidates = [(p, a) for p in ctx.opponent_pokemon_in_play()
                  for a in getattr(_def_for(p.archetype_id), "abilities", []) if isinstance(a, Attack)]
    if candidates:
        picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
        if picked is not None:
            await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="2bc3b194-cc0e-574b-abf3-617de17a4bf8",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Pendulum Influence",
            game_text="Flip a coin. If heads, choose an attack from 1 of your opponent's Pokémon in play and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=pendulum_influence,
        ),
        Attack(
            title="Psychic Sphere",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
