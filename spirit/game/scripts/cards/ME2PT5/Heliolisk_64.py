"""Heliolisk (ME2PT5 64 -- JP M2a 053; English ASC/229, ASC/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import def_for, subtypes_for


def _played_this_turn(ctx, display_name) -> bool:
    for archetype_id, _name, _type in ctx.session.turn_state.trainers_played:
        if getattr(def_for(archetype_id), "display_name", None) == display_name:
            return True
    return False
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)



def _frilled_condition(board, player_id, pokemon) -> bool:
    from spirit.game.data_utils import def_for as _d
    ts = getattr(board, "turn_state", None)
    return ts is not None and any(getattr(_d(a), "display_name", None) == "Canari"
                                  for a, _n, _t in ts.trainers_played)


async def frilled_generator(ctx):
    if not _played_this_turn(ctx, "Canari"):
        return
    await su.search_attach_energy(_basic_lightning, count=2, to_self=True,
                                  prompt="Choose up to 2 Basic Lightning Energy cards to attach to this Pokémon.")(ctx)


async def powerful_bolt(ctx):
    n = len(ctx.attached_energies(ctx.attacker))
    heads = sum(1 for r in await ctx.flip_coins(n, "Powerful Bolt") if r) if n else 0
    if heads:
        await ctx.deal_damage(70 * heads)


card = PokemonCardDef(
    guid="7181c65e-af2f-54fa-bd29-44948b0e6d34",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Ability(
            title="Frilled Generator",
            game_text="Once during your turn, if you played Canari from your hand this turn, you may use this Ability. Search your deck for up to 2 Basic Lightning Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_frilled_condition,
            effect=frilled_generator,
        ),
        Attack(
            title="Powerful Bolt",
            game_text="Flip a coin for each Energy attached to this Pokémon. This attack does 70 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=powerful_bolt,
        ),
    ],
)
