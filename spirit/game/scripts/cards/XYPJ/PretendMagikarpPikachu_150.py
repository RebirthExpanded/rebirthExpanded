"""Pretend Magikarp Pikachu (XYPJ 150 -- JP XYP 150; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

_discard_all = ac.self_energy_discard_attack(all_energy=True)


card = PokemonCardDef(
    guid="cc4bb5c5-7871-5711-85d4-98b641477937",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendMagikarpPikachu.Name",
    display_name="Pretend Magikarp Pikachu",
    searchable_by=["Pretend Magikarp Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=150,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Try Splashing",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ac.flip_or_nothing(),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_discard_all,
        ),
    ],
)
