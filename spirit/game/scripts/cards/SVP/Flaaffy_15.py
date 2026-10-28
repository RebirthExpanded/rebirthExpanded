"""Flaaffy (SVP 15 -- JP SVP 025; English SVP/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="a15946fa-86de-54c5-a320-1d7aef52564a",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=["Flaaffy", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Static Shock",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Extreme Current",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
