"""Pawmo (ME2 33 -- JP M2 033; English PFL/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="d54ff94e-2cc3-529a-85eb-567eaba76409",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    display_name="Pawmo",
    searchable_by=["Pawmo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="ME2",
    regulation_mark="I",
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
            title="Electric Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
        ),
    ],
)
