"""Larvesta (BWPJ 310 -- JP WAK 010; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7f2080d5-4b8f-50cf-8b88-85ece1e270c0",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    display_name="Larvesta",
    searchable_by=["Larvesta", "Basic"],
    subtypes=["Basic"],
    collector_number=310,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=636,
    abilities=[
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 10 more damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_damage(coins=2, bonus_per_heads=10),
        ),
    ],
)
