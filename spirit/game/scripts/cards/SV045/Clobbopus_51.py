"""Clobbopus (SV045 51 -- JP SV4K 035; English PAF/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def feint(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="9a42bda9-031b-511d-b920-4efc3b794a6a",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    display_name="Clobbopus",
    searchable_by=["Clobbopus", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=852,
    abilities=[
        Attack(
            title="Feint",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=feint,
        ),
    ],
)
