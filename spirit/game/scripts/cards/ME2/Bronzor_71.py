"""Bronzor (ME2 71 -- JP M2 059; English PFL/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="0832ded9-12c1-51df-b771-c965201cc3aa",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=436,
    abilities=[
        Attack(
            title="Iron Defense",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.flip_protection(prevent=True),
        ),
        Attack(
            title="Rollout",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
