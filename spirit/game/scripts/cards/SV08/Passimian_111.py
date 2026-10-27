"""Passimian (SV08 111 -- JP SV7a 031; English SSP/111). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon_in_play


card = PokemonCardDef(
    guid="adf2778a-8cf3-5d8d-b092-ba64db5b6b00",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Attack(
            title="Coordinated Throwing",
            game_text="This attack does 20 damage for each of your Basic Pokémon in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine", is_basic_pokemon_in_play), 20),
        ),
    ],
)
