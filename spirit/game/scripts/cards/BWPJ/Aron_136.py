"""Aron (BWPJ 136 -- JP BWP 136; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="295e1daa-cb41-5b9a-bd97-ebf4bfb3b339",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    display_name="Aron",
    searchable_by=["Aron", "Basic"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=304,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Iron Defense",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=pc.flip_protection(),
        ),
    ],
)
