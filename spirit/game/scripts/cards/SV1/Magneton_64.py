"""Magneton (SV1 64 -- JP SV1V 027; English SVI/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="db1fce18-d884-5b84-ae62-71d09fa7936e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Lightning Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Explosion",
            game_text="This Pokémon also does 90 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=90,
            effect=ac.recoil_attack(90),
        ),
    ],
)
