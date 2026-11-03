"""Tapu Koko (SMD 7 -- JP SMD 007; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_energy_card


def _lightning_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


def _benched(pokemon) -> bool:
    return pokemon._containing_area_name() == "bench"


card = PokemonCardDef(
    guid="91a763df-269d-527d-a53f-c5ae98440ccf",
    key="SMD",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKoko.Name",
    display_name="Tapu Koko",
    searchable_by=["Tapu Koko", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SMD",
    regulation_mark="A",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=785,
    abilities=[
        Attack(
            title="Electro Maker",
            game_text="Attach a Lightning Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.attach_from_discard(_lightning_energy, target=_benched, prompt="Choose a Lightning Energy card to attach to 1 of your Benched Pokémon."),
        ),
        Attack(
            title="Mach Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)
