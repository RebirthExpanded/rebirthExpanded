"""Seaking (ME5 14 -- JP M5 013; English PBL/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def hydro_jet(ctx):
    n = ac.count_energy("self", PokemonTypes.WATER)(ctx)
    if n > 0:
        await ac.snipe_attack(30 * n, pool="any")(ctx)


card = PokemonCardDef(
    guid="e6a3b9ab-10ec-5fa7-9e1d-d8db01ba9cee",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seaking.Name",
    display_name="Seaking",
    searchable_by=["Seaking", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    family_id=118,
    abilities=[
        Attack(
            title="Hydro Jet",
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon for each Water Energy attached to this Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=hydro_jet,
        ),
    ],
)
