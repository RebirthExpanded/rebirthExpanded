"""Gimmighoul (SV045 44 -- JP SV4a 099; English PAF/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="e6e7607e-3574-5450-b5ad-081a90ff79eb",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    display_name="Gimmighoul",
    searchable_by=["Gimmighoul", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=999,
    abilities=[
        Attack(
            title="Chest-ouflage",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
