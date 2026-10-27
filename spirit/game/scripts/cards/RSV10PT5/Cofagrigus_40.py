"""Cofagrigus (RSV10PT5 40 -- JP SV11W 037; English WHT/123, WHT/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def extended_damagriiigus(ctx):
    pool = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    targets = ctx.opponent_pokemon_in_play()
    if not pool or not targets:
        return
    source = await ctx.choose_pokemon(pool, "Choose 1 of your Benched Pokémon to move all damage counters from")
    if source is None:
        return
    dest = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon to move them to")
    if dest is not None:
        await ctx.move_damage_counters(source, dest)


card = PokemonCardDef(
    guid="011c010d-d794-5186-bc00-6558f20427c8",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Attack(
            title="Extended Damagriiigus",
            game_text="Move all damage counters from 1 of your Benched Pokémon to 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=extended_damagriiigus,
        ),
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
