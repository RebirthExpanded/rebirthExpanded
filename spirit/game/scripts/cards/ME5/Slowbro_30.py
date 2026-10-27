"""Slowbro (ME5 30 -- JP M5 029; English MEP/83, PBL/30, PBL/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _empty_hand(ctx) -> bool:
    return not ctx.hand()


card = PokemonCardDef(
    guid="86b769d5-f853-5b00-8c46-fc96d57a7a62",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="All Out",
            game_text="If you have no cards in your hand, this attack does 160 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_empty_hand, 160),
        ),
        Attack(
            title="Zen Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)
