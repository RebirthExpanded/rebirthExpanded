"""Drifloon (ME6A 61 -- JP M6a 061; English 30C/136, 30C/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="778fe202-04fd-5bc3-9842-02cb4058cae0",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=425,
    abilities=[
        Attack(
            title="Float Up",
            game_text="You may shuffle this Pokémon and all attached cards into your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=su.remove_self_from_play("deck", optional=True),
        ),
    ],
)
