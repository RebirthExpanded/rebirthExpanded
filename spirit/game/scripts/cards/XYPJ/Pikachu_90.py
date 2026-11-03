"""Pikachu (XYPJ 90 -- JP XYP 090; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

_discard_all = ac.self_energy_discard_attack(all_energy=True)


card = PokemonCardDef(
    guid="ededbd60-839b-5789-a274-ff55c3e10d2a",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=90,
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
            title="Thunderbolt",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=100,
            effect=_discard_all,
        ),
    ],
)
