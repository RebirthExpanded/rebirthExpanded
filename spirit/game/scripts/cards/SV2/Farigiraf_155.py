"""Farigiraf (SV2 155 -- JP SV2D 060; English PAL/155, PAL/228). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def either_face(ctx):
    index = await ctx.choose("Choose a player", ["You", "Your opponent"])
    pid = ctx.opponent_id if index == 1 else ctx.player_id
    hand = list(ctx.hand(pid))
    if hand:
        await ctx.shuffle_into_deck(hand, pid)
    else:
        await ctx.shuffle_deck(pid)
    await ctx.draw_cards(4, player_id=pid)


card = PokemonCardDef(
    guid="a9b01c78-4ceb-5823-a26e-5d56bbe864e6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farigiraf.Name",
    display_name="Farigiraf",
    searchable_by=["Farigiraf", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=155,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    family_id=203,
    abilities=[
        Attack(
            title="Either Face",
            game_text="Choose a player. That player shuffles their hand into their deck and draws 4 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=either_face,
        ),
        Attack(
            title="Power Beam",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
