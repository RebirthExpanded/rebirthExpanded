"""Dubwool (SV07 125 -- JP SV7 087; English SCR/125). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def knock_over(ctx):
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="3c91d5f2-0790-5382-bdd7-2cb016744b85",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dubwool.Name",
    display_name="Dubwool",
    searchable_by=["Dubwool", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=125,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    family_id=831,
    abilities=[
        Ability(
            title="Soft Wool",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30),
        ),
        Attack(
            title="Knock Over",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=knock_over,
        ),
    ],
)
