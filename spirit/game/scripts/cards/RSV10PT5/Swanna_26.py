"""Swanna (RSV10PT5 26 -- JP SV11W 023; English WHT/110, WHT/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bf011663-47fc-5ad3-9b61-2202456df92e",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name",
    display_name="Swanna",
    searchable_by=["Swanna", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    family_id=580,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
