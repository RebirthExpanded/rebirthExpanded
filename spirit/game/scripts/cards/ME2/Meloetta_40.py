"""Meloetta (ME2 40 -- JP MBD 004; English MEP/26, PFL/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def soothing_melody(ctx):
    pool = [p for p in ctx.my_bench() if _of_type(p, PokemonTypes.PSYCHIC) and _counters(ctx.board, p) > 0]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Psychic Pokémon to heal 120 damage from")
    if target is not None:
        await ctx.heal(120, target)


card = PokemonCardDef(
    guid="6efcae92-9a2d-57aa-ac31-c0f777b5a94d",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=648,
    abilities=[
        Attack(
            title="Soothing Melody",
            game_text="Heal 120 damage from 1 of your Benched Psychic Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=soothing_melody,
        ),
        Attack(
            title="Magical Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
