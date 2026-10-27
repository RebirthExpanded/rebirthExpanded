"""Granbull (ME2 38 -- JP MBD 002; English PFL/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="cac3c8c8-2a8a-5623-9ad9-2ec750e17d85",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name",
    display_name="Granbull",
    searchable_by=["Granbull", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    family_id=209,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Finishing Blow",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 90),
        ),
    ],
)
