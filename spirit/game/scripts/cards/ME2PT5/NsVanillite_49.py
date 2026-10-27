"""N's Vanillite (ME2PT5 49 -- JP M2a 037; English ASC/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="fd559748-50fa-5b25-af1b-2e3c8cab25eb",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanillite.Name",
    display_name="N's Vanillite",
    searchable_by=["N's Vanillite", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=582,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=2, prompt="Choose up to 2 Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Icy Snow",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
