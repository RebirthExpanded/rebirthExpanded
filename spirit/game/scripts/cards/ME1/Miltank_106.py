"""Miltank (ME1 106 -- JP M1L 054; English MEG/106). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def bellyful_of_milk(ctx):
    results = await ctx.flip_coins(2, "Bellyful of Milk")
    if not (results and all(results)):
        return
    damaged = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose 1 of your Pokémon to heal all damage from")
    if target is not None:
        await ctx.heal(_counters(ctx.board, target) * 10, target)


card = PokemonCardDef(
    guid="bc60ec78-6810-5042-bc4a-dbee19e6f74e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Attack(
            title="Bellyful of Milk",
            game_text="Flip 2 coins. If both of them are heads, heal all damage from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=bellyful_of_milk,
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
