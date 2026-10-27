"""Heliolisk (ME1 53 -- JP M1S 035; English MEG/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bc75dcd7-0d64-5be1-b728-e4d4949342bd",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Dazzle Blast",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Head Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
