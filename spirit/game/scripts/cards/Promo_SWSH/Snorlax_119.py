"""Snorlax (Promo_SWSH 119 -- JP SP 156; English SP/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5cf843d2-9308-540a-82fa-544f12ba46f6",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Single Strike"],
    subtypes=["Basic", "Single Strike"],
    collector_number=119,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Attack(
            title="Slap Push",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Single Strike Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=ac.recoil_attack(30),
        ),
    ],
)
