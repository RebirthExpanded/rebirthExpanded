"""Corvisquire (SV2 165 -- JP SV2P 064; English PAL/165). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6914f66c-a919-5e11-941c-fc1f05a7c12f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    display_name="Corvisquire",
    searchable_by=["Corvisquire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=165,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Glide",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
