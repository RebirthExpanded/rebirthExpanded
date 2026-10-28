"""Venusaur ex (SV07 1 -- JP SV2a 003; English MEW/182, MEW/198, MEW/3, SCR/1). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _tranquil_condition(board, player_id, pokemon) -> bool:
    return board.active_pokemon(player_id) is pokemon and any(_counters(board, p) > 0 for p in board.pokemon_in_play(player_id))


async def tranquil_flower(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 60 damage from")
        if target is not None:
            await ctx.heal(60, target)


card = PokemonCardDef(
    guid="76bb6cfc-72ec-534c-834e-6d0fbf84f549",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaurex.Name",
    display_name="Venusaur ex",
    searchable_by=["Venusaur ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=1,
    set_code="SV07",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Tranquil Flower",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may heal 60 damage from 1 of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_tranquil_condition,
            effect=tranquil_flower,
        ),
        Attack(
            title="Dangerous Toxwhip",
            game_text="Your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=ac.condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)
