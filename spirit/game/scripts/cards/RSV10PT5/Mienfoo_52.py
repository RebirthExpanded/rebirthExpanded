"""Mienfoo (RSV10PT5 52 -- JP SV11W 049; English WHT/133, WHT/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4ad9aee2-6b7f-515e-a09c-6c575d13de8f",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    display_name="Mienfoo",
    searchable_by=["Mienfoo", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=619,
    abilities=[
        Attack(
            title="Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
