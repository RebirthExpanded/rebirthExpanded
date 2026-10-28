"""Meditite (SV1 110 -- JP SV1S 038; English SVI/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def feint(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="d2ade93b-b676-5016-ae8a-426d17c8d097",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    display_name="Meditite",
    searchable_by=["Meditite", "Basic"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=307,
    abilities=[
        Attack(
            title="Feint",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=feint,
        ),
    ],
)
