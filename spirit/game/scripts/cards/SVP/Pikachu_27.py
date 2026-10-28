"""Pikachu (SVP 27 -- JP SVP 001; English SVP/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0b027524-bab1-5139-9e22-9235994eaf9c",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Adventuring Together",
            game_text="This attack does 10 more damage for each of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_bench("mine"), 10, base=30),
        ),
    ],
)
