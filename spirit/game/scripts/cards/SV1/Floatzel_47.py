"""Floatzel (SV1 47 -- JP SV1S 016; English SVI/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="c8671a7c-ab98-5c5f-9d21-bf3343e1a4f5",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name",
    display_name="Floatzel",
    searchable_by=["Floatzel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    family_id=418,
    abilities=[
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage for each Water Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.WATER), 20, base=50),
        ),
    ],
)
