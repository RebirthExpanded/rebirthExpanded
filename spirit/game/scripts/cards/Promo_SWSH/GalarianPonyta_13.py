"""Galarian Ponyta (Promo_SWSH 13 -- JP SP 025; English SP/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="4661dcad-030b-5816-8982-0604adbb7aaf",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPonyta.Name",
    display_name="Galarian Ponyta",
    searchable_by=["Galarian Ponyta", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=77,
    abilities=[
        Attack(
            title="Heal Pulse",
            game_text="Heal 30 damage from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.heal_targets(30, "choice"),
        ),
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
