"""Minun (SV4 61 -- JP SV3a 015; English PAR/194, PAR/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _buddy_applies(ctx) -> bool:
    me = ctx.source
    attacher = getattr(ctx, "attaching_player_id", None)
    receiver = getattr(ctx, "energy_receiver", None)
    return (attacher is not None and attacher != me.owning_player_id and receiver is not None
            and any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Plusle"
                    for p in ctx.board.pokemon_in_play(me.owning_player_id)))


async def buddy_pulse(ctx):
    if not _buddy_applies(ctx):
        return
    receiver = ctx.energy_receiver
    mark = (ctx.session.turn_state.turn_number, getattr(ctx.attached_energy, "entity_id", None))
    if getattr(receiver, "_buddy_pulse", None) == mark:
        return
    receiver._buddy_pulse = mark
    await ctx.deal_damage(20, target=receiver, apply_modifiers=False, as_counters=True, is_attack=False)


card = PokemonCardDef(
    guid="31f404a6-7c29-5ae9-88ce-62bd1b2e1df3",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=312,
    abilities=[
        Ability(
            title="Buddy Pulse",
            game_text="If you have Plusle in play, whenever your opponent attaches an Energy card from their hand to 1 of their Pokémon, put 2 damage counters on that Pokémon. The effect of Buddy Pulse doesn't stack.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=buddy_pulse,
        ),
        Attack(
            title="Speed Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)
