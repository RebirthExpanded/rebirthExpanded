"""Eevee VMAX (Promo_SWSH 87 -- JP SP 101; English SP/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="401ba74e-f9e6-5909-b01d-e47999d74b53",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeVMAX.Name",
    display_name="Eevee VMAX",
    searchable_by=["Eevee VMAX", "VMAX"],
    subtypes=["VMAX"],
    collector_number=87,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeV.Name",
    family_id=133,
    abilities=[
        Attack(
            title="G-Max Cuddle",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=ac.smokescreen_attack(),
        ),
    ],
)
