"""Chandelure (SV3 38 -- JP SVD 017; English OBF/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="38ad1ca6-a45c-5475-b9ec-7d5d30ed2afe",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Combustion Chain",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 50, base=10),
        ),
        Attack(
            title="Heat Blast",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
        ),
    ],
)
