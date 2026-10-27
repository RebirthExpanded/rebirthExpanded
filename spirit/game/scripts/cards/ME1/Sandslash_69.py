"""Sandslash (ME1 69 -- JP M1L 021; English MEG/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="da3041ff-4206-5fb6-9b26-f23458f65a76",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash",
    searchable_by=["Sandslash", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Attack(
            title="Sand Attack",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to use an attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.smokescreen_attack(),
        ),
        Attack(
            title="Mud Shot",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
