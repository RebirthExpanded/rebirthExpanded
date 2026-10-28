"""Larvesta (SV3 40 -- JP SV1a 012; English OBF/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="af34d623-24f0-5cdb-afef-458c430f7be0",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    display_name="Larvesta",
    searchable_by=["Larvesta", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=636,
    abilities=[
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Take Down",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.recoil_attack(10),
        ),
    ],
)
