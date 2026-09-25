"""Poipole (SM - Lost Thunder 107/214 -- JP SM8 047/095).

Basic Psychic Pokemon, Ultra Beast. HP 70, weakness Psychic x2, retreat 1.

  Eye Opener  [C]     Look at your face-down Prize cards.
  Peck        [CC] 20

Only the owner sees them (the view-only browser), and they are re-hidden
afterwards so the client does not keep drawing them face up in the pile.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.attributes import GameSequence
from spirit.game.data_utils import Attack, PokemonCardDef


async def eye_opener(ctx):
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = [c for c in (area.children if area else []) if not c.face_up]
    if not prizes:
        return
    await ctx.flush_choreography()
    session = ctx.session
    await session.prompt_view_cards(ctx.player_id, ctx.source.entity_id, prizes,
                                    prompt="Your Prize cards")
    owner = session.players.get(ctx.player_id)
    if owner is not None:
        await session.send_game_sequence(
            [owner], GameSequence.GROUPED_MOVE,
            [session._attributes_reset_msg(c.entity_id) for c in prizes])


card = PokemonCardDef(
    guid="34eace0e-c9a2-5280-9bac-532cc9beef62",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    display_name="Poipole",
    searchable_by=['Poipole', 'Basic', 'Ultra Beast', 'Poipole'],
    subtypes=['Basic', 'Ultra Beast'],
    collector_number=107,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=803,
    abilities=[
        Attack(title="Eye Opener", game_text="Look at your face-down Prize cards.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=eye_opener),
        Attack(title="Peck", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
