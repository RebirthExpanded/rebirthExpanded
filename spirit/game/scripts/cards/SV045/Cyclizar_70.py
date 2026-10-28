"""Cyclizar (SV045 70 -- JP SV4a 136; English PAF/195, PAF/70). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="00c17e8a-aaaf-507a-9b81-f307cdd3ec8e",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name",
    display_name="Cyclizar",
    searchable_by=["Cyclizar", "Basic"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=967,
    abilities=[
        Attack(
            title="Acceleration Drive",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
