"""Tyranitar (SV2 135 -- JP SV2D 052; English PAL/135, PAL/222). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def dread_mountain(ctx):
    await ctx.deal_damage()
    top = list(ctx.deck_top(4))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="d983f911-ce7f-5589-b510-12b998659001",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=135,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Rout",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_bench("opponent"), 30, base=30),
        ),
        Attack(
            title="Dread Mountain",
            game_text="Discard the top 4 cards of your deck.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=230,
            effect=dread_mountain,
        ),
    ],
)
