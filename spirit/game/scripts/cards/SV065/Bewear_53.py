"""Bewear (SV065 53 -- JP SV6a 053; English SFA/53, SFA/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="9080b3f1-c2d5-5070-a42d-a53f054edac4",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Attack(
            title="Power Charger",
            game_text="Search your deck for a Basic Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=su.search_attach_energy(is_basic_energy_card, count=1, to_self=True, prompt="Choose a Basic Energy card to attach to this Pokémon."),
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
