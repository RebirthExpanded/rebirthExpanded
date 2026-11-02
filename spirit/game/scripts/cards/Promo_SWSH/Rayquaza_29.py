"""Rayquaza (Promo_SWSH 29 -- JP SP 003; English SP/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bd7f44c9-105e-5a38-a388-620dad246fdf",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=384,
    abilities=[
        Attack(
            title="Jaw Lock",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
