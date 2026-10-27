"""Sizzlipede (SV05 36 -- JP SV5K 010; English TEF/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c1e55938-bb51-5426-aab0-abad3c4c7dfa",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    display_name="Sizzlipede",
    searchable_by=["Sizzlipede", "Basic"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=850,
    abilities=[
        Attack(
            title="Heat Dive",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
