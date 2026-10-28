"""Tarountula (SV2 16 -- JP SV2D 007; English PAL/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="405c5d20-a748-56c5-9380-20426b157714",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name",
    display_name="Tarountula",
    searchable_by=["Tarountula", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=917,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
