"""Poncho-wearing Pikachu (XYPJ 208 -- JP XYP 208; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="65df434d-603e-5a86-93b2-8261fdc0b58c",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PonchowearingPikachu.Name",
    display_name="Poncho-wearing Pikachu",
    searchable_by=["Poncho-wearing Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=208,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Crimson Dive?",
            game_text="Flip a coin. If tails, this Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=90,
            effect=ac.flip_damage(tails_self_damage=30),
        ),
    ],
)
