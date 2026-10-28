"""Nidorina (SV035 30 -- JP SV2a 030; English MEW/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


card = PokemonCardDef(
    guid="03762530-dc4f-518a-a499-089ec8e49155",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    display_name="Nidorina",
    searchable_by=["Nidorina", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranFemale.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Fetch Family",
            game_text="Search your deck for up to 3 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=su.search_to_hand(is_pokemon_card, count=3, reveal=True, prompt="Choose up to 3 Pokémon."),
        ),
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
