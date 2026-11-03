"""Ash's Pikachu-GX (SMD 5 -- JP SMD 005; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ef73638c-7fca-5d39-aa0d-798184b1b04a",
    key="SMD",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AshsPikachuGX.Name",
    display_name="Ash's Pikachu-GX",
    searchable_by=["Ash's Pikachu-GX", "Basic", "GX"],
    subtypes=["Basic", "GX"],
    collector_number=5,
    set_code="SMD",
    regulation_mark="A",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
        Attack(
            title="Thunderbolt-GX",
            game_text="Discard all Energy from this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=200,
            effect=ac.self_energy_discard_attack(all_energy=True),
            gx=True,
        ),
    ],
)
