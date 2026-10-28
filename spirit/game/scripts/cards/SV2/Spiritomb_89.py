"""Spiritomb (SV2 89 -- JP SV2D 028; English PAF/158, PAL/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc

from spirit.game.session.effects import full_stack


async def _back_to_hand(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    if me in ctx.knockouts:
        return
    if ctx.board.active_pokemon(ctx.player_id) is me and not ctx.my_bench():
        return
    await ctx.put_in_hand(full_stack(me), reveal=False)
from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.effects import is_basic_pokemon_in_play


def _basic_v(pokemon, carrier) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or []
    return is_basic_pokemon_in_play(pokemon) and "V" in subs


card = PokemonCardDef(
    guid="59b042b3-9f1d-5c43-8f11-9d4a29c3fda6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=442,
    abilities=[
        Ability(
            title="Fettered in Misfortune",
            game_text="Basic Pokémon V in play (both yours and your opponent's) have no Abilities.",
            passive=pc.ability_lock_passive(_basic_v),
        ),
        Attack(
            title="Fade Out",
            game_text="Put this Pokémon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_back_to_hand,
        ),
    ],
)
