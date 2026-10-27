"""Team Rocket's Flaaffy (SV10 73 -- JP SV10 035; English DRI/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="deb5d30e-857f-5b3c-8d39-9b7c304f9f30",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsFlaaffy.Name",
    display_name="Team Rocket's Flaaffy",
    searchable_by=["Team Rocket's Flaaffy", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
