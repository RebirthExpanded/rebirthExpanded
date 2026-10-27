"""Seadra (SV065 11 -- JP SV6a 011; English SFA/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="8a501cc1-e6fe-5bef-92ef-2951b6c52b4c",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    display_name="Seadra",
    searchable_by=["Seadra", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Call for Backup",
            game_text="Search your deck for up to 3 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=su.search_to_hand(is_pokemon_card, count=3, reveal=True, prompt="Choose up to 3 Pokémon."),
        ),
        Attack(
            title="Sharp Fin",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
