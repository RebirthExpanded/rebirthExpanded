"""Team Rocket's Grimer (SV10 123 -- JP SV10 067; English DRI/123). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import full_stack


async def corrosive_sludge(ctx):
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
    guid="a8a0184b-9b6a-5098-b4fa-8678f66d1422",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGrimer.Name",
    display_name="Team Rocket's Grimer",
    searchable_by=["Team Rocket's Grimer", "Basic"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=88,
    abilities=[
        Attack(
            title="Corrosive Sludge",
            game_text="At the end of your opponent's next turn, discard the Defending Pokémon and all attached cards.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=corrosive_sludge,
        ),
    ],
)
