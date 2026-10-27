"""Naclstack (ME1 83 -- JP M1L 035; English MEG/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def rock_hurl(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="fa3d473e-cdb6-54b2-a679-a46a4ecdcd76",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    display_name="Naclstack",
    searchable_by=["Naclstack", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    family_id=932,
    abilities=[
        Attack(
            title="Rock Hurl",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=rock_hurl,
        ),
    ],
)
