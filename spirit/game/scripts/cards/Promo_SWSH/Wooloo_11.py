"""Wooloo (Promo_SWSH 11 -- JP SP 004; English SP/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="554ec8db-4455-5cd1-a6c4-6ea6a7596eec",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    display_name="Wooloo",
    searchable_by=["Wooloo", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=831,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.flip_protection(prevent=True),
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
