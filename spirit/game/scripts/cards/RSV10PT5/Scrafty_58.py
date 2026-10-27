"""Scrafty (RSV10PT5 58 -- JP SV11W 055; English WHT/139, WHT/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def ruffians_attack(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if _of_type(p, PokemonTypes.DARKNESS))
    heads = sum(1 for r in await ctx.flip_coins(n, "Ruffians Attack") if r) if n else 0
    if heads:
        await ctx.deal_damage(60 * heads)


card = PokemonCardDef(
    guid="6d08b007-262f-530a-8605-2c92bfd3913f",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Ruffians Attack",
            game_text="Flip a coin for each Darkness Pokémon you have in play. This attack does 60 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
            damage_operator="x",
            effect=ruffians_attack,
        ),
    ],
)
