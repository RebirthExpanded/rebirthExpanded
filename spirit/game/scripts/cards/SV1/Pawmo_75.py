"""Pawmo (SV1 75 -- JP SV1V 035; English PAF/143, SVI/75). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3e60ba6d-1b90-5cf3-80d2-d7b80303eeb1",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    display_name="Pawmo",
    searchable_by=["Pawmo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    family_id=921,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Head Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
