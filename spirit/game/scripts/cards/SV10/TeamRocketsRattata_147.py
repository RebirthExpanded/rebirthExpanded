"""Team Rocket's Rattata (SV10 147 -- JP SV10 076; English DRI/147). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5c3ff772-0e0b-5784-9e3f-6f78dc82e33a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsRattata.Name",
    display_name="Team Rocket's Rattata",
    searchable_by=["Team Rocket's Rattata", "Basic"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=19,
    abilities=[
        Attack(
            title="Dangerous Incisors",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
