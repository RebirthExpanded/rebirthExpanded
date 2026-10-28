"""Bellsprout (SV035 69 -- JP SV2a 069; English MEW/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2db9301a-5f19-58db-9c23-1bf8b096792d",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    display_name="Bellsprout",
    searchable_by=["Bellsprout", "Basic"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Cut",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
