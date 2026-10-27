"""Corphish (ME1 33 -- JP M1L 018; English MEG/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5635d83f-7de3-5d4c-8d43-f271df70037f",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    display_name="Corphish",
    searchable_by=["Corphish", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=341,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Take Down",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
