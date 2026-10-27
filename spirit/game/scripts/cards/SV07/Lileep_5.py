"""Lileep (SV07 5 -- JP SV7 003; English SCR/145, SCR/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="150bad50-7add-57df-a267-e0972c59d2e0",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep",
    searchable_by=["Lileep", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueRootFossil.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
