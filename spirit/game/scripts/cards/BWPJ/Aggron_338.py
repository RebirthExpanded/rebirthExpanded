"""Aggron (BWPJ 338 -- JP WAK 038; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="500062c6-9ef6-5ea1-8b4f-033f61de4eb8",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=338,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Mega Punch",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Upper Thrust",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
