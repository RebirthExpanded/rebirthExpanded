"""Weepinbell (SV035 70 -- JP SV2a 070; English MEW/70). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fb19e3be-aa52-5e5c-89f7-def8f752e92d",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    display_name="Weepinbell",
    searchable_by=["Weepinbell", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Cut",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Spray Fluid",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
