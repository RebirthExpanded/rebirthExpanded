"""Cresselia (SV065 21 -- JP SV6a 021; English SFA/21, SFA/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

import random


async def healing_pirouette(ctx):
    for p in ctx.my_pokemon_in_play():
        await ctx.heal(20, p)


async def crescent_purge(ctx):
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    down = [c for c in (area.children if area else []) if not c.face_up]
    if down and await ctx.ask_yes_no("Turn 1 of your face-down Prize cards face up for 80 more damage?"):
        prize = random.choice(down)
        prize.face_up = True
        for viewer in (ctx.player_id, ctx.opponent_id):
            ctx._queue(ctx.session._entity_introduced_msg(prize), viewer_id=viewer)
        await ctx.deal_damage(160)
    else:
        await ctx.deal_damage(80)


card = PokemonCardDef(
    guid="66d768bf-0cfd-511f-800b-10d8f26922bc",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=488,
    abilities=[
        Attack(
            title="Healing Pirouette",
            game_text="Heal 20 damage from each of your Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=healing_pirouette,
        ),
        Attack(
            title="Crescent Purge",
            game_text="You may turn 1 of your face-down Prize cards face up. If you do, this attack does 80 more damage. (That Prize card remains face up for the rest of the game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=80,
            damage_operator="+",
            effect=crescent_purge,
        ),
    ],
)
