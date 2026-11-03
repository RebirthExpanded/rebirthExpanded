"""Pidove (BWPJ 406 -- JP CS1 006; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="2852b62d-256b-5aaf-95fe-8d808be9570a",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove", "Basic"],
    subtypes=["Basic"],
    collector_number=406,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=519,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.debuff_defender_attacks(20),
        ),
        Attack(
            title="Gust",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
