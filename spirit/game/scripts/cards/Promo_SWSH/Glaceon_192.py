"""Glaceon (Promo_SWSH 192 -- JP SP 216; English SP/192). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6b77760b-6153-5731-a66d-98a9f7715ddc",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    display_name="Glaceon",
    searchable_by=["Glaceon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=192,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Hail",
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=ac.damage_all_opponents(20),
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="During your next turn, this Pokémon can't use Frosty Typhoon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
