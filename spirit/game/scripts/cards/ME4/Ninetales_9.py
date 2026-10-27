"""Ninetales (ME4 9 -- JP M4 009; English CRI/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def nine_tailed_transfer(ctx):
    target = ctx.opponent_active()
    damaged = [p for p in ctx.my_bench() if _counters(ctx.board, p) > 0]
    if target is None or not damaged:
        return
    source = await ctx.choose_pokemon(damaged, "Choose a Benched Pokémon to move all damage counters from")
    if source is None:
        return
    n = _counters(ctx.board, source)
    moved = await ctx.remove_damage_counters(source, n)
    if moved:
        await ctx.deal_damage(10 * moved, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="fb507e55-2796-5820-a275-9b67be70b643",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Nine-Tailed Transfer",
            game_text="Move all damage counters from 1 of your Benched Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            effect=nine_tailed_transfer,
        ),
        Attack(
            title="Will-O-Wisp",
            game_text="",
            cost={PokemonTypes.FIRE: 2},
            damage=70,
        ),
    ],
)
