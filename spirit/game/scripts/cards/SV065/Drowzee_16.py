"""Drowzee (SV065 16 -- JP SV6a 016; English SFA/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def eerie_gaze(ctx):
    await ctx.deal_damage()
    if ctx.hand(ctx.opponent_id):
        await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)


card = PokemonCardDef(
    guid="406148b3-83d4-5904-bd92-853a18d65748",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=96,
    abilities=[
        Attack(
            title="Eerie Gaze",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=eerie_gaze,
        ),
    ],
)
