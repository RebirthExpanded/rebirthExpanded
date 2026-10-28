"""Vespiquen ex (SV3 96 -- JP SV3 051; English OBF/212, OBF/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def healing_pheromone(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 60 damage from")
        if target is not None:
            await ctx.heal(60, target)


async def phantom_queen(ctx):
    await ctx.deal_damage()
    for p in list(ctx.opponent_bench()):
        if _counters(ctx.board, p) > 0:
            await ctx.deal_damage(30, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="86c50dad-e3a4-5ca4-8bee-e7704ff73e82",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquenex.Name",
    display_name="Vespiquen ex",
    searchable_by=["Vespiquen ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=96,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Healing Pheromone",
            game_text="Heal 60 damage from 1 of your Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=healing_pheromone,
        ),
        Attack(
            title="Phantom Queen",
            game_text="Put 3 damage counters on each of your opponent's Benched Pokémon that has any damage counters on it.",
            cost={PokemonTypes.GRASS: 3},
            damage=200,
            effect=phantom_queen,
        ),
    ],
)
