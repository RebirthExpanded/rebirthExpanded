"""Mewtwo (MF 10 -- JP MF 010; English 30C/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="34476fa5-5470-5d0d-9d69-e0106d6b4ff9",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=150,
    abilities=[
        Attack(
            title="Empower",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.attach_from_discard(is_basic_energy_card, count=2, target="choice", minimum=0, prompt="Attach up to 2 Basic Energy cards from your discard pile to 1 of your Pokémon."),
        ),
        Attack(
            title="Psydrive",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
