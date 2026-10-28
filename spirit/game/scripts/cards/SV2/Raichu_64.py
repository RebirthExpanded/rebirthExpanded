"""Raichu (SV2 64 -- JP SV2D 018; English PAL/211, PAL/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


card = PokemonCardDef(
    guid="4203f5ec-8c27-5ac6-bd79-4c782012de42",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=172,
    abilities=[
        Attack(
            title="Electrocharge",
            game_text="Search your deck for up to 2 Basic Lightning Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_attach_energy(_basic_lightning, count=2, to_self=True, prompt="Choose up to 2 Basic Lightning Energy cards to attach to this Pokémon."),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
