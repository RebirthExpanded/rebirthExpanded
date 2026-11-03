"""Virizion (BWPJ 305 -- JP WAK 005; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="c622c660-5ab3-5cbc-b91f-b36a15b952ad",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion", "Basic"],
    subtypes=["Basic"],
    collector_number=305,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=640,
    abilities=[
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=20),
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=su.heal_attack(20),
        ),
    ],
)
