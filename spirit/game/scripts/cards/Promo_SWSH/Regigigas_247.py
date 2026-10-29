"""Regigigas (Promo_SWSH 247 -- JP SP 266; English SP/247). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="c113ca7f-c36c-56f5-ba25-6caaa43d9425",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic"],
    subtypes=["Basic"],
    collector_number=247,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Limber Up",
            game_text="Attach a basic Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.attach_from_discard(is_basic_energy_card, count=1, target="self", minimum=0),
        ),
        Attack(
            title="Double Impact",
            game_text="Flip 2 coins. This attack does 120 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=120),
        ),
    ],
)
