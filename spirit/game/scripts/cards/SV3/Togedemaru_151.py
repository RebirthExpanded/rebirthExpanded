"""Togedemaru (SV3 151 -- JP SVD 083; English OBF/151). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="bdf9ad3e-3951-5ecf-b570-8f55a5b199c5",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name",
    display_name="Togedemaru",
    searchable_by=["Togedemaru", "Basic"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=777,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.flip_protection(prevent=True),
        ),
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
