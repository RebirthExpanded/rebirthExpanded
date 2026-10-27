"""Slowpoke (MEP 86 -- JP MP 070; English MEP/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="5a6dbfd2-4779-5551-883f-6b3d8e230ac6",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=79,
    abilities=[
        Ability(
            title="Oblivious",
            game_text="This Pokémon can't be Confused.",
            passive=pc.condition_immunity_passive(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Psypower",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
