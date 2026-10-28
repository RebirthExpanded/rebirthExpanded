"""Mawile (SV3 89 -- JP SVD 051; English OBF/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="1b477837-4954-5544-9c62-c2543e91587c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=303,
    abilities=[
        Attack(
            title="Mischievous Crunch",
            game_text="This attack does 30 damage for each Psychic Energy attached to this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("self", _PT.PSYCHIC), 30),
        ),
    ],
)
