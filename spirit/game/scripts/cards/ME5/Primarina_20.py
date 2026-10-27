"""Primarina (ME5 20 -- JP M5 019; English PBL/20, PBL/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _enriching_applies(ctx) -> bool:
    return bool(getattr(ctx, "evolved_from_hand", True)) and any(
        _counters(ctx.board, p) > 0 for p in ctx.my_pokemon_in_play())


async def enriching_melody(ctx):
    damaged = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if not damaged or not await ctx.ask_yes_no("Use Enriching Melody?"):
        return
    target = await ctx.choose_pokemon(damaged, "Choose a Pokémon to heal all damage from")
    if target is not None:
        await ctx.heal(10 * _counters(ctx.board, target), target)


card = PokemonCardDef(
    guid="b1f76b4d-d800-5f76-aaf0-11cec2d5cea0",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primarina.Name",
    display_name="Primarina",
    searchable_by=["Primarina", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    family_id=728,
    abilities=[
        Ability(
            title="Enriching Melody",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Heal all damage from 1 of your Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            trigger_applies=_enriching_applies,
            effect=enriching_melody,
        ),
        Attack(
            title="Aqua Return",
            game_text="Shuffle this Pokémon and all attached cards into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=su.remove_self_from_play("deck"),
        ),
    ],
)
