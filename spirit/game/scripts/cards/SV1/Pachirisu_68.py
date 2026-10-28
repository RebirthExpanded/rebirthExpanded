"""Pachirisu (SV1 68 -- JP SV1V 029; English PAF/138, SVI/208, SVI/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def everyone_discharge(ctx):
    n = sum(1 for p in ctx.my_bench() if _of_type(p, PokemonTypes.LIGHTNING))
    await ctx.deal_damage(10 + 20 * n, ignore_weakness=True)


card = PokemonCardDef(
    guid="8af538d4-64d8-575b-a584-f9938a2ecf1a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=417,
    abilities=[
        Ability(
            title="Electricity Pouches",
            game_text="This Pokémon can't be Paralyzed.",
            passive=pc.condition_immunity_passive(SpecialConditions.PARALYZED),
        ),
        Attack(
            title="Everyone Discharge",
            game_text="This attack does 20 more damage for each of your Benched Lightning Pokémon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=everyone_discharge,
        ),
    ],
)
