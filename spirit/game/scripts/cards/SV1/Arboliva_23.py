"""Arboliva (SV1 23 -- JP SV1S 008; English PAF/104, SVI/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def enriching_oil(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if not pool or not await ctx.ask_yes_no("Use Enriching Oil?"):
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal all damage from")
    if target is not None:
        await ctx.heal(10 * _counters(ctx.board, target), target)


card = PokemonCardDef(
    guid="5fe449a8-4860-5bcb-b4c8-518ec87d7de2",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arboliva.Name",
    display_name="Arboliva",
    searchable_by=["Arboliva", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Ability(
            title="Enriching Oil",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may heal all damage from 1 of your Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=enriching_oil,
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)
