"""Altaria (SV08 134 -- JP SV7a 041; English SSP/134). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="b442c7d9-f660-5c24-a88e-c5e6880d5abf",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Attack(
            title="Humming Charge",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=su.search_attach_energy(is_basic_energy_card, count=2, prompt="Choose up to 2 Basic Energy cards to attach to your Pokémon."),
        ),
        Attack(
            title="Cotton Wings",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=100,
            effect=pc.flip_protection(prevent=True),
        ),
    ],
)
