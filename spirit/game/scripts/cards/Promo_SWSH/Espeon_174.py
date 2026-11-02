"""Espeon (Promo_SWSH 174 -- JP SP 179; English SP/174). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="df425330-9fca-5e55-8a82-39a444cf1de6",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=174,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 40 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 40, base=10),
        ),
    ],
)
