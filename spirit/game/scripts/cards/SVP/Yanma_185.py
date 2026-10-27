"""Yanma (SVP 185 -- JP SVP 163; English SVP/185). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def silent_wing(ctx):
    await ctx.deal_damage()
    if ctx.hand(ctx.opponent_id):
        await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)


card = PokemonCardDef(
    guid="1984e7d2-f2c4-50aa-b2ce-d80b50ac4ce8",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    display_name="Yanma",
    searchable_by=["Yanma", "Basic"],
    subtypes=["Basic"],
    collector_number=185,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=193,
    abilities=[
        Attack(
            title="Silent Wing",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=silent_wing,
        ),
    ],
)
