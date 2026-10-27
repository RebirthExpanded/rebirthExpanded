"""Togedemaru (SV09 50 -- JP SVM 045; English JTG/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="7d8fea31-fa3b-5312-856e-1ff19b9cad14",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name",
    display_name="Togedemaru",
    searchable_by=["Togedemaru", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=777,
    abilities=[
        Attack(
            title="Toge Spark",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
