"""Pikachu (XYPJ 281 -- JP XYP 281; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="a7f0ccd9-4b4a-555c-934b-f39f168cf5a1",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=281,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 10 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.debuff_defender_attacks(10),
        ),
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
