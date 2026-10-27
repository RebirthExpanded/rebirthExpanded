"""Cradily (SV07 6 -- JP SV7 004; English SCR/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


_CHOICES = [("Burned", SpecialConditions.BURNED), ("Confused", SpecialConditions.CONFUSED),
            ("Poisoned", SpecialConditions.POISONED)]


def _selective_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    return other is not None and board.active_pokemon(other) is not None


async def selective_slime(ctx):
    results = await ctx.flip_coins(1, "Selective Slime")
    target = ctx.opponent_active()
    if not (results and results[0]) or target is None:
        return
    index = await ctx.choose("Choose a Special Condition", [label for label, _ in _CHOICES])
    if isinstance(index, int) and 0 <= index < len(_CHOICES):
        await ctx.apply_special_condition(target, _CHOICES[index][1])


def _conditions(ctx) -> int:
    d = ctx.opponent_active()
    return len(d.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) if d is not None else 0


card = PokemonCardDef(
    guid="3f2870fd-ab19-59f5-ad0c-f2c68ac64849",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name",
    display_name="Cradily",
    searchable_by=["Cradily", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=345,
    abilities=[
        Ability(
            title="Selective Slime",
            game_text="Once during your turn, you may flip a coin. If heads, choose Burned, Confused, or Poisoned. Your opponent's Active Pokémon is now affected by that Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_selective_condition,
            effect=selective_slime,
        ),
        Attack(
            title="Miasma Wind",
            game_text="This attack does 100 damage for each Special Condition affecting your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=100,
            damage_operator="x",
            effect=ac.damage_per(_conditions, 100),
        ),
    ],
)
