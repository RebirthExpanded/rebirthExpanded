"""Dipplin (SV10 17 -- JP SV9a 010; English DRI/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def energy_loop(ctx):
    await ctx.deal_damage()
    pool = ctx.attached_energies(ctx.attacker)
    if pool:
        picks = await ctx.choose_cards(list(pool), 1, minimum=1, prompt="Choose an Energy to put into your hand")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="ba657af3-920c-577d-a2b5-f378b682a298",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    display_name="Dipplin",
    searchable_by=["Dipplin", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Energy Loop",
            game_text="Put an Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=energy_loop,
        ),
    ],
)
