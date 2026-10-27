"""Sawk (RSV10PT5 49 -- JP SV11W 046; English WHT/130, WHT/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


async def rising_chop(ctx):
    if _defender_ex(ctx):
        await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="80c98f01-af38-5e80-894c-d15c3b2436e0",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name",
    display_name="Sawk",
    searchable_by=["Sawk", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=539,
    abilities=[
        Attack(
            title="Elbow Strike",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Rising Chop",
            game_text="If your opponent's Active Pokémon isn't a Pokémon ex, this attack does nothing. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=90,
            effect=rising_chop,
        ),
    ],
)
