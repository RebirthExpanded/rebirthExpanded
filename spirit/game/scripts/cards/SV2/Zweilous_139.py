"""Zweilous (SV2 139 -- JP SV1a 058; English PAL/139). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="520024fb-2c41-5cbb-8839-1e68c7b37ea1",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    display_name="Zweilous",
    searchable_by=["Zweilous", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=139,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for up to 2 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_pokemon_card, count=2, reveal=True, prompt="Choose up to 2 Pokémon."),
        ),
        Attack(
            title="Headbutt Bounce",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
