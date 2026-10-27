"""Jynx (ME5 32 -- JP M5 030; English PBL/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import full_stack


async def intense_kiss(ctx):
    d = ctx.opponent_active()
    if d is None or ctx.effects_blocked(d):
        return
    target_id = d.entity_id
    owner = ctx.player_id

    async def _discard(session):
        target = session.board_state.get_entity(target_id)
        parent = getattr(target, "parent", None)
        if target is None or parent is None or parent.get_attribute(AttrID.NAME) not in ("activePokemonArea", "bench"):
            return
        from spirit.game.session.effects import EffectContext
        c = EffectContext(session, owner, ctx.source, ctx.ability)
        await c.discard_cards(full_stack(target))
        await c.flush_choreography()
        await session.enforce_bench_capacity()

    ctx.schedule_at_checkup(1, _discard)


card = PokemonCardDef(
    guid="5045d9bb-ecbe-53fb-81fa-f36854e95184",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=238,
    abilities=[
        Attack(
            title="Intense Kiss",
            game_text="At the end of your opponent's next turn, discard the Defending Pokémon and all attached cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=intense_kiss,
        ),
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
