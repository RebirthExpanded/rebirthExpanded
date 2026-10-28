"""Flamigo (SV4 106 -- JP SV3a 032; English PAR/106). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="94723979-a264-515c-84b7-e84a41e834f4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name",
    display_name="Flamigo",
    searchable_by=["Flamigo", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Attack(
            title="Peck",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Combat Beak",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(ac.count_bench("opponent"), 20, base=20),
        ),
    ],
)
